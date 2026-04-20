from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app

client = TestClient(app)

# 1. Create fake Adzuna data that perfectly mimics Jerri's function output
MOCK_ADZUNA_DATA = {
    "total_found": 3,
    "jobs": [
        {"title": "Python Developer", "company": "Tech Corp", "location": "Remote"},
        {"title": "Remote Backend Engineer", "company": "Tech Corp", "location": "New York"},
        {"title": "Data Scientist", "company": "Data Inc", "location": "Texas - Remote"}
    ]
}

# 2. Use @patch to intercept the function exactly where it is imported in your routes
@patch("app.modules.stats.routes.fetch_jobs_from_adzuna")
def test_get_stats_success(mock_fetch):
    # Tell the intercepted function to return our fake data instead of calling the internet
    mock_fetch.return_value = MOCK_ADZUNA_DATA

    # 3. Simulate a web browser asking for stats
    response = client.get("/stats?q=python")

    # 4. Assert that your math engine processed the fake data correctly
    assert response.status_code == 200
    data = response.json()
    
    assert data["total_jobs"] == 3
    
    # We expect 3 remote jobs because "Remote" is in two locations and one title
    assert data["remote_jobs"] == 3 
    
    # "Tech Corp" appears twice, so it should be the top company
    assert data["top_companies"][0] == "Tech Corp"

@patch("app.modules.stats.routes.fetch_jobs_from_adzuna")
def test_get_stats_empty_data(mock_fetch):
    # Test the edge case where Adzuna finds absolutely nothing
    mock_fetch.return_value = {"total_found": 0, "jobs": []}

    response = client.get("/stats?q=impossible_job_search")
    
    assert response.status_code == 200
    data = response.json()
    assert data["total_jobs"] == 0
    assert data["top_companies"] == []