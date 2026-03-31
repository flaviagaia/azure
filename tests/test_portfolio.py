from __future__ import annotations

import unittest

from src.projects import bundle_reports


class AzurePortfolioTestCase(unittest.TestCase):
    def test_bundle_reports_has_three_projects(self) -> None:
        report = bundle_reports()
        self.assertEqual(len(report["projects"]), 3)
        names = {project["project_name"] for project in report["projects"]}
        self.assertEqual(
            names,
            {
                "payment_anomaly_stream_azure",
                "enterprise_policy_search_azure",
                "claims_approval_workflow_azure",
            },
        )

    def test_metrics_are_present(self) -> None:
        report = bundle_reports()
        projects = {project["project_name"]: project for project in report["projects"]}
        self.assertGreater(projects["payment_anomaly_stream_azure"]["events_processed"], 100)
        self.assertGreater(projects["enterprise_policy_search_azure"]["documents_indexed"], 2)
        self.assertGreater(projects["claims_approval_workflow_azure"]["claims_processed"], 0)


if __name__ == "__main__":
    unittest.main()

