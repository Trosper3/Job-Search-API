from fastapi import APIRouter

router = APIRouter (
    tags=["jobs"]
)

@router.get("")
async def get_jobs(q: str = ""):
    """
    Skeleton route for fetching jobs.
    Later, this will call the Adzuna Job Search API."""

    return {"message": f"Yay! Jobs endpoint is working", "query": q}
