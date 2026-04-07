from fastapi import APIRouter, Query

from app.modules.jobs.service import fetch_jobs_from_adzuna

router = APIRouter (
    tags=["jobs"]
)

@router.get("")
async def get_jobs(q: str = Query(..., description="The job title or keyword to search for")):
    return await fetch_jobs_from_adzuna(q)