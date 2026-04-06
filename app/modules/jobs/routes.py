from fastapi import APIRouter, Query

router = APIRouter (
    tags=["jobs"]
)

@router.get("")
async def get_jobs(q: str = Query(..., description="The job title or keyword to search for")):
    """
    Skeleton route for fetching jobs.
    Later, this will call the Adzuna Job Search API."""

    return {"message": "Yay! Jobs endpoint is working", "query": q}