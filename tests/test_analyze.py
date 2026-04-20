"""Tests for the /analyze endpoint."""

from fastapi.testclient import TestClient
from unittest.mock import patch

from app.main import app


client = TestClient(app)


def test_analyze_valid_request():
    """Returns mocked skills for a valid description payload."""
    expected = {"skills": ["python", "fastapi"]}
    description = "Python developer needed with FastAPI, SQL, and Docker experience."

    with patch("app.modules.analyze.routes.analyze_description", return_value=expected) as mock_analyze:
        response = client.post(
            "/analyze",
            json={"description": description},
        )

    assert response.status_code == 200
    assert response.json() == expected
    mock_analyze.assert_called_once_with(description)


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


def test_analyze_whitespace_only_description():
    """Returns bad request when description contains only whitespace."""
    with patch("app.modules.analyze.routes.analyze_description") as mock_analyze:
        response = client.post("/analyze", json={"description": "   "})

    assert response.status_code == 400
    assert response.json()["detail"] == "description must not be empty"
    mock_analyze.assert_not_called()
