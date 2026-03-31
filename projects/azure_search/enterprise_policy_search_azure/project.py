from __future__ import annotations

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def build_corpus() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "doc_id": "POL-1001",
                "title": "Travel Expense Policy",
                "content": "Employees must submit travel receipts within ten business days and require manager approval for international travel.",
                "domain": "finance_policy",
            },
            {
                "doc_id": "POL-1002",
                "title": "Information Security Policy",
                "content": "Multifactor authentication is mandatory for privileged accounts and sensitive systems must be reviewed quarterly.",
                "domain": "security_policy",
            },
            {
                "doc_id": "POL-1003",
                "title": "Remote Work Guidelines",
                "content": "Remote employees must maintain approved devices, secure network access, and keep weekly availability updated.",
                "domain": "hr_policy",
            },
            {
                "doc_id": "POL-1004",
                "title": "Procurement Approval Matrix",
                "content": "Purchases above five thousand dollars require procurement review and director approval before vendor onboarding.",
                "domain": "procurement_policy",
            },
        ]
    )


def run() -> dict:
    df = build_corpus()
    query = "approval for travel expenses and receipt submission deadline"
    vectorizer = TfidfVectorizer(ngram_range=(1, 2))
    matrix = vectorizer.fit_transform(df["title"] + " " + df["content"])
    query_vector = vectorizer.transform([query])
    similarities = cosine_similarity(query_vector, matrix)[0]
    top_idx = similarities.argsort()[::-1][:3]
    return {
        "project_name": "enterprise_policy_search_azure",
        "azure_services": ["Azure AI Search", "Azure App Service", "Azure SQL Database"],
        "documents_indexed": int(len(df)),
        "top_match_doc_id": df.iloc[top_idx[0]]["doc_id"],
        "top_match_score": round(float(similarities[top_idx[0]]), 4),
        "retrieved_documents": df.iloc[top_idx]["doc_id"].tolist(),
    }

