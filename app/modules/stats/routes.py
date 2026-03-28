from fastapi import APIRouter
from .service import calculate_job_stats

router = APIRouter(
    tags=["stats"]
)

@router.get("/stats")
async def get_job_stats(q: str = ""):
    """
    Computes statistics for a given job search query.
    """
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

    stats = calculate_job_stats(mock_adzuna_data)
    return stats