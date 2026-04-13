"""Pytest configuration and shared fixtures."""
import pytest
from unittest.mock import AsyncMock, patch


@pytest.fixture
def mock_adzuna_response():
