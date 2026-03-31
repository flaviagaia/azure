from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest


def build_dataset(seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    size = 900
    df = pd.DataFrame(
        {
            "event_id": [f"EVT-{1000 + idx}" for idx in range(size)],
            "amount": rng.gamma(shape=2.4, scale=45.0, size=size),
            "velocity_10m": rng.poisson(1.7, size=size),
            "geo_distance_km": rng.gamma(shape=2.0, scale=18.0, size=size),
            "merchant_risk": rng.uniform(0.05, 0.95, size=size),
            "night_flag": rng.binomial(1, 0.22, size=size),
        }
    )
    anomaly_mask = rng.choice([0, 1], size=size, p=[0.93, 0.07]).astype(bool)
    df.loc[anomaly_mask, "amount"] *= rng.uniform(3.0, 7.0, anomaly_mask.sum())
    df.loc[anomaly_mask, "velocity_10m"] += rng.integers(4, 11, anomaly_mask.sum())
    df.loc[anomaly_mask, "geo_distance_km"] *= rng.uniform(2.5, 5.0, anomaly_mask.sum())
    df["target_anomaly"] = anomaly_mask.astype(int)
    return df


def run() -> dict:
    df = build_dataset()
    features = df[["amount", "velocity_10m", "geo_distance_km", "merchant_risk", "night_flag"]]
    contamination = max(float(df["target_anomaly"].mean()), 0.03)
    model = IsolationForest(n_estimators=220, contamination=contamination, random_state=42)
    model.fit(features)
    score = -model.decision_function(features)
    normalized = (score - score.min()) / (score.max() - score.min() + 1e-9)
    flagged = (normalized >= np.quantile(normalized, 0.93)).astype(int)
    precision = ((flagged == 1) & (df["target_anomaly"] == 1)).sum() / max((flagged == 1).sum(), 1)
    recall = ((flagged == 1) & (df["target_anomaly"] == 1)).sum() / max((df["target_anomaly"] == 1).sum(), 1)
    return {
        "project_name": "payment_anomaly_stream_azure",
        "azure_services": ["Event Hubs", "Stream Analytics", "Azure Machine Learning", "Power BI"],
        "events_processed": len(df),
        "anomaly_rate": round(float(df["target_anomaly"].mean()), 4),
        "flagged_events": int(flagged.sum()),
        "precision": round(float(precision), 4),
        "recall": round(float(recall), 4),
    }

