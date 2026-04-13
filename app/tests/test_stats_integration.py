from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app

client = TestClient(app)

MOCK_ADZUNA_DATA = {
    "total_found": 3,
    "jobs": [
        {"title": "Python Developer", "company": "TechFlow", "location": "Remote"},
        {"title": "Backend Engineer", "company": "TechFlow", "location": "New York"},
        {"title": "Data Analyst", "company": "DataWorks", "location": "Texas - Remote"},
    ],
}

@patch("app.modules.stats.routes.fetch_jobs_from_adzuna")
def test_stats_endpoint_success(mock_fetch):
    mock_fetch.return_value = MOCK_ADZUNA_DATA

    response = client.get("/stats?q=python")

    assert response.status_code == 200
    data = response.json()

    assert data["total_jobs"] == 3
    assert data["remote_jobs"] == 2
    assert "TechFlow" in data["top_companies"]