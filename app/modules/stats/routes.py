from fastapi import APIRouter
from app.modules.stats.service import calculate_job_stats


from app.modules.jobs.service import fetch_jobs_from_adzuna

router = APIRouter()

@router.get("/stats")
async def get_stats(q: str = "python"):
    """
    Fetches live job data from Adzuna and calculates market statistics.
    The 'q' parameter defaults to 'python' if the user doesn't provide one.
    """
    # 1. Call the jobs module service to securely fetch live Adzuna data
    live_data = await fetch_jobs_from_adzuna(q)
    
    # 2. Pass the live data into our math engine
    final_stats = calculate_job_stats(live_data)
    
    # 3. Return the calculated business insights
    return final_stats