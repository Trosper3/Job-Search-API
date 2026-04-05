from fastapi import APIRouter, HTTPException, Query
from app.modules.jobs.service import fetch_jobs

router = APIRouter (
    tags=["jobs"]
)

@router.get("")
async def get_jobs(q: str = Query(..., description="Enter job title or keywords to search for")):
    """
Fetch jobs from Adzuna API based on the search query provided by the user.
Example: GET /jobs?q=python
    """

    try:
        results = await fetch_jobs(q)
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))