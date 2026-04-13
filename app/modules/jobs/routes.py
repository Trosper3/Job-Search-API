from fastapi import APIRouter, HTTPException, Query
from app.modules.jobs.service import fetch_jobs_from_adzuna

router = APIRouter (
    tags=["jobs"]
)

@router.get("")
async def get_jobs(q: str = Query(..., description="The job title or keyword to search for")):
    try:
        results = await fetch_jobs_from_adzuna(q)
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))