from fastapi import APIRouter
from .service import calculate_job_stats

router = APIRouter(
    tags=["jobs"]
)

@router.get("")
async def get_jobs(q: str = ""):
    """
    Skeleton route for fetching jobs.
    Later, this will call the Adzuna Job Search API.
    """
    return {"message": f"Jobs endpoint is working !", "query": q}

@router.get("/stats")
async def get_job_stats(q: str = ""):
    """
    Computes statistics for a given job search query.
    """
    # Temporary mock data to test the math logic 
    # until the live Adzuna API call is implemented
    mock_adzuna_data = {
        "count": 3,
        "results": [
            {
                "title": "Python Backend Engineer",
                "company": {"display_name": "TechFlow"},
                "location": {"display_name": "Remote"},
                "description": "This is a fully remote position."
            },
            {
                "title": "Data Scientist",
                "company": {"display_name": "Health Analytics"},
                "location": {"display_name": "Austin, TX"},
                "description": "On-site role in Texas."
            },
            {
                "title": "Junior Python Developer",
                "company": {"display_name": "TechFlow"},
                "location": {"display_name": "Remote"},
                "description": "Work from anywhere."
            }
        ]
    }

    # Pass the mock data into the calculation function
    stats = calculate_job_stats(mock_adzuna_data)

    return stats