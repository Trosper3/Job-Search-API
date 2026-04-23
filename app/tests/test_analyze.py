"""Tests for the /analyze endpoint."""

from fastapi.testclient import TestClient
from unittest.mock import patch

from app.main import app


client = TestClient(app)


def test_analyze_valid_request():
    """Returns 405 because POST /analyze was removed in favor of live GET flow."""
    response = client.post(
        "/analyze",
        json={"description": "Python developer needed with FastAPI"},
    )

    assert response.status_code == 405


def test_analyze_live_jobs_success():
    """Returns analyzed skills derived from live jobs payload."""
    mocked_jobs = {
        "total_found": 2,
        "jobs": [
            {"description": "Python FastAPI SQL Docker"},
            {"description": "Python APIs and cloud deployment"},
        ],
    }
    expected = {"skills": ["python", "apis", "cloud"]}

    with (
        patch("app.modules.analyze.routes.fetch_jobs_from_adzuna", return_value=mocked_jobs) as mock_fetch,
        patch("app.modules.analyze.routes.analyze_jobs_data", return_value=expected) as mock_analyze_jobs,
    ):
        response = client.get("/analyze", params={"q": "python"})

    assert response.status_code == 200
    assert response.json() == expected
    mock_fetch.assert_called_once_with("python")
    mock_analyze_jobs.assert_called_once_with(mocked_jobs)


def test_analyze_live_jobs_requires_query():
    """Returns validation error when q is missing for live analyze endpoint."""
    response = client.get("/analyze")

    assert response.status_code == 422
