from fastapi.testclient import TestClient
from app.main import app

# Create a TestClient instance for testing the FastAPI application
client = TestClient(app)

def test_jobs_endpoint():
    # Test the /jobs endpoint with a valid query
    response = client.get("/jobs?q=python")

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Make sure the response contains a list of jobs
    data = response.json()

    #verify that the strucutre of the data is correct
    assert "Total_found" in data
    assert "jobs" in data
    assert isinstance(data["jobs"], list)

def test_missing_query():
    # Test the /jobs endpoint without providing the required query parameter
    response = client.get("/jobs")

    # Assert that the response status code is 422 (Unprocessable Entity) due to missing query parameter
    assert response.status_code == 422

