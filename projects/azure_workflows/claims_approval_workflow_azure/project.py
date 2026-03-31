from __future__ import annotations

import pandas as pd


def build_claims() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {"claim_id": "CLM-1001", "claim_type": "travel", "amount": 420.0, "documents_complete": 1, "policy_match": 1, "requires_manual_review": 0},
            {"claim_id": "CLM-1002", "claim_type": "medical", "amount": 1800.0, "documents_complete": 1, "policy_match": 0, "requires_manual_review": 1},
            {"claim_id": "CLM-1003", "claim_type": "equipment", "amount": 620.0, "documents_complete": 0, "policy_match": 1, "requires_manual_review": 1},
            {"claim_id": "CLM-1004", "claim_type": "travel", "amount": 210.0, "documents_complete": 1, "policy_match": 1, "requires_manual_review": 0},
        ]
    )


def run() -> dict:
    df = build_claims()
    auto_approved = df[(df["documents_complete"] == 1) & (df["policy_match"] == 1) & (df["requires_manual_review"] == 0)]
    manual_queue = df[df["requires_manual_review"] == 1]
    return {
        "project_name": "claims_approval_workflow_azure",
        "azure_services": ["Logic Apps", "Azure Functions", "Blob Storage", "API Management"],
        "claims_processed": int(len(df)),
        "auto_approved": int(len(auto_approved)),
        "manual_review_queue": int(len(manual_queue)),
        "auto_approval_rate": round(float(len(auto_approved) / len(df)), 4),
    }

