"""Tests for the /analyze endpoint."""

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_analyze_valid_request():
    """Returns extracted skills for a valid description payload."""
    response = client.post(
        "/analyze",
        json={
            "description": "Python developer needed with FastAPI, SQL, and Docker experience."
        },
    )

    assert response.status_code == 200
    payload = response.json()
    assert "skills" in payload
    assert "python" in payload["skills"]
    assert "fastapi" in payload["skills"]


def test_analyze_missing_fields():
    """Returns validation error when required fields are missing."""
    response = client.post("/analyze", json={})

    assert response.status_code == 422


def test_analyze_invalid_json():
    """Returns validation error when payload is invalid JSON."""
    response = client.post(
        "/analyze",
        content='{"description": "python"',
        headers={"Content-Type": "application/json"},
    )

    assert response.status_code == 422
