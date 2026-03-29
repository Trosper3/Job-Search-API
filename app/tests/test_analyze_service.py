"""Unit tests for analyze service logic."""

from app.modules.analyze.service import analyze_description, extract_keywords


def test_extract_keywords_returns_ranked_keywords():
    """Returns frequent, filtered keywords from a description."""
    description = "Python FastAPI Python SQL Docker and the"

    result = extract_keywords(description)

    assert result[0] == "python"
    assert "fastapi" in result
    assert "sql" in result
    assert "docker" in result


def test_extract_keywords_returns_empty_for_stop_words_only():
    """Returns no keywords when all tokens are filtered out."""
    result = extract_keywords("the and of in to with")

    assert result == []


def test_analyze_description_wraps_skills_payload():
    """Wraps extracted keywords inside the expected response shape."""
    result = analyze_description("Python developer with FastAPI")

    assert "skills" in result
    assert isinstance(result["skills"], list)
