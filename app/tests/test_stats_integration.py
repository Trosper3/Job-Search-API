from fastapi.testclient import TestClient
from app.main import app  # Imports your actual FastAPI application

# Create a fake web browser to test your app
client = TestClient(app)

def test_stats_endpoint_success(mock_adzuna_response):
    # 1. ACT: Send a fake GET request to the stats route
    response = client.get("/stats") 

    # 2. ASSERT: Check that the server responded with a "200 OK" success code
    assert response.status_code == 200
    
    # 3. ASSERT: Check that the JSON body sent to the browser is correct
    data = response.json()
    assert data["Total_jobs"] == 3
    assert data["Remote_jobs"] == 2
    assert "TechFlow" in data["top_companies"]