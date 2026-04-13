"""Tests for the /jobs endpoint and jobs service."""

import asyncio
from unittest.mock import AsyncMock, Mock, patch

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.modules.jobs import service as jobs_service


client = TestClient(app)


def test_jobs_endpoint_success(mock_adzuna_response):
    """Returns the expected payload for a valid jobs query."""
    response = client.get("/jobs", params={"q": "python"})

    assert response.status_code == 200

    assert response.json() == {
        "total_found": 1,
        "jobs": [
            {
                "id": "123",
                "title": "Python Developer",
                "company": "IBM",
                "location": "Remote",
                "description": "Build APIs",
                "url": "https://example.com/job-123"
            }
        ]
    }


def test_jobs_endpoint_requires_query():
    """Returns validation error when the required query parameter is missing."""
    response = client.get("/jobs")

    assert response.status_code == 422


def test_fetch_jobs_from_adzuna_returns_normalized_jobs():
    """Normalizes Adzuna results into the API response shape."""
    mock_payload = {
        "results": [
            {
                "id": "job-1",
                "title": "Python Developer",
                "company": {"display_name": "Acme"},
                "location": {"display_name": "Remote"},
                "description": "Build APIs",
                "redirect_url": "https://example.com/job-1",
            },
            {
                "id": "job-2",
                "title": "Data Engineer",
                "description": "Work with pipelines",
                "redirect_url": "https://example.com/job-2",
            },
        ]
    }

    mock_response = Mock(status_code=200)
    mock_response.json.return_value = mock_payload

    mock_client = AsyncMock()
    mock_client.get = AsyncMock(return_value=mock_response)

    with (
        patch.object(jobs_service, "ADZUNA_APP_ID", "test_app_id"),
        patch.object(jobs_service, "ADZUNA_APP_KEY", "test_app_key"),
        patch("app.modules.jobs.service.httpx.AsyncClient") as mock_async_client,
    ):
        mock_async_client.return_value.__aenter__.return_value = mock_client

        result = asyncio.run(jobs_service.fetch_jobs_from_adzuna("python"))

    assert result == {
        "total_found": 2,
        "jobs": [
            {
                "id": "job-1",
                "title": "Python Developer",
                "company": "Acme",
                "location": "Remote",
                "description": "Build APIs",
                "url": "https://example.com/job-1",
            },
            {
                "id": "job-2",
                "title": "Data Engineer",
                "company": None,
                "location": None,
                "description": "Work with pipelines",
                "url": "https://example.com/job-2",
            },
        ],
    }
    mock_client.get.assert_awaited_once()


def test_fetch_jobs_from_adzuna_raises_on_non_200_response():
    """Raises an HTTPException when Adzuna does not return success."""
    mock_response = Mock(status_code=500)
    mock_response.json.return_value = {}

    mock_client = AsyncMock()
    mock_client.get = AsyncMock(return_value=mock_response)

    with (
        patch.object(jobs_service, "ADZUNA_APP_ID", "test_app_id"),
        patch.object(jobs_service, "ADZUNA_APP_KEY", "test_app_key"),
        patch("app.modules.jobs.service.httpx.AsyncClient") as mock_async_client,
    ):
        mock_async_client.return_value.__aenter__.return_value = mock_client

        with pytest.raises(Exception) as exc_info:
            asyncio.run(jobs_service.fetch_jobs_from_adzuna("python"))

    assert getattr(exc_info.value, "status_code", None) == 500
    assert getattr(exc_info.value, "detail", None) == "Failed to fetch jobs from external API"
