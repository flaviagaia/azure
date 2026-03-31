from __future__ import annotations

from projects.azure_search.enterprise_policy_search_azure.project import run as run_enterprise_policy_search
from projects.azure_streaming.payment_anomaly_stream_azure.project import run as run_payment_anomaly_stream
from projects.azure_workflows.claims_approval_workflow_azure.project import run as run_claims_approval_workflow


def bundle_reports() -> dict:
    return {
        "projects": [
            run_payment_anomaly_stream(),
            run_enterprise_policy_search(),
            run_claims_approval_workflow(),
        ]
    }

