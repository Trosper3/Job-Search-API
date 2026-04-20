"""Tests for the main FastAPI application."""

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_app_metadata_is_configured():
    """Exposes the expected application metadata from the FastAPI instance."""
    assert app.title == "Job Search API"
    assert app.version == "1.0.0"


def test_root_endpoint_returns_welcome_message():
    """Returns the expected welcome payload from the root endpoint."""
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Job Search API!"}
