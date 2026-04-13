"""Pytest configuration and shared fixtures."""
import pytest
from unittest.mock import AsyncMock, Mock, patch


@pytest.fixture
def mock_adzuna_response():
    #mock data for Adzuna to return
    mock_payload = {
        "results": [
            {
                "id": "12345",
                "title": "Software Engineer",
                "company": {"display_name": "Apple Inc."},
                "location": {"display_name": "Cupertino, CA"},
                "description": "We are looking for a Software Engineer to join our team.",
                "redirect_url": "https://www.apple.com",
            }
        ]
    }

    # mock HTTP response
    mock_response = Mock(status_code=200)
    mock_response.json.return_value = mock_payload

    # mock AsyncClient
    mock_client = AsyncMock()
    mock_client.get = AsyncMock(return_value=mock_response)

    # patch the client and credientials globally for all tests
    with (
        patch("app.modules.jobs.service.ADZUNA_APP_ID", "test_app_id"),
        patch("app.modules.jobs.service.ADZUNA_APP_KEY", "test_app_key"),
        patch("app.modules.jobs.service.httpx.AsyncClient") as mock_async_client
    ):
        # set the mock client to be returned whenever AsyncClient is instantiated
        mock_async_client.return_value.__aenter__.return_value = mock_client
        yield mock_client