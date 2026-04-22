from fastapi import APIRouter, Query

from app.modules.analyze.service import analyze_jobs_data
from app.modules.jobs.service import fetch_jobs_from_adzuna


router = APIRouter(
    tags=["analyze"]
)


@router.get("")
async def analyze_live_jobs(q: str = Query(..., description="The job title or keyword to analyze")):
    """Fetch live Adzuna jobs and extract common skills from descriptions."""
    live_jobs = await fetch_jobs_from_adzuna(q)
    return analyze_jobs_data(live_jobs)
