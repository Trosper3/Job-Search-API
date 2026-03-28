"""Business logic for analyzing job descriptions."""

from collections import Counter
import re


STOP_WORDS = {
	"a",
	"an",
	"and",
	"are",
	"as",
	"at",
	"be",
	"by",
	"for",
	"from",
	"in",
	"is",
	"it",
	"of",
	"on",
	"or",
	"that",
	"the",
	"to",
	"with",
	"you",
	"your",
	"we",
	"our",
}


def extract_keywords(text: str, max_keywords: int = 10) -> list[str]:
	"""Return the most relevant keyword tokens from a job description."""
	tokens = re.findall(r"[A-Za-z][A-Za-z0-9+#.-]*", text.lower())
	filtered_tokens = [
		token
		for token in tokens
		if token not in STOP_WORDS and len(token) > 1
	]

	if not filtered_tokens:
		return []

	counts = Counter(filtered_tokens)
	ranked_keywords = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
	return [keyword for keyword, _ in ranked_keywords[:max_keywords]]


def analyze_description(description: str) -> dict[str, list[str]]:
	"""Extract skills from a raw job description."""
	return {"skills": extract_keywords(description)}
