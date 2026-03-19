"""Pytest configuration and shared fixtures."""
import pytest


@pytest.fixture
def sample_fixture():
    """Sample fixture for testing."""
    return {"test": "data"}
