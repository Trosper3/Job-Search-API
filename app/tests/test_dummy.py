"""Dummy test to verify pytest setup."""
import pytest


def test_example():
    """Simple passing test."""
    assert True


def test_addition():
    """Test basic arithmetic."""
    assert 1 + 1 == 2


def test_with_fixture(sample_fixture):
    """Test using a fixture."""
    assert sample_fixture["test"] == "data"
