from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app.modules.analyze.service import analyze_description


router = APIRouter(
	tags=["analyze"]
)


class AnalyzeRequest(BaseModel):
	"""Input payload for description analysis."""

	description: str = Field(..., min_length=1)


@router.post("")
async def analyze_job_text(payload: AnalyzeRequest):
	"""Analyze a job description and return extracted skills."""
	if not payload.description.strip():
		raise HTTPException(status_code=400, detail="description must not be empty")

	return analyze_description(payload.description)
