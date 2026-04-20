import httpx
import os
from fastapi import HTTPException

# In a real app, these would be loaded from your teammate's Doppler setup or a .env file
ADZUNA_APP_ID = os.getenv("ADZUNA_APP_ID")
ADZUNA_APP_KEY = os.getenv("ADZUNA_APP_KEY")
BASE_URL = "https://api.adzuna.com/v1/api/jobs/us/search/1"

async def fetch_jobs_from_adzuna(query: str):
    """
    Makes an async HTTP GET request to the Adzuna API.
    """
    if not ADZUNA_APP_ID or not ADZUNA_APP_KEY:
        raise HTTPException(status_code=500, detail="Adzuna credentials are not configured / correct")
    
    # Set up the parameters for the API call
    params = {
        "app_id": ADZUNA_APP_ID,
        "app_key": ADZUNA_APP_KEY,
        "what": query,
        "results_per_page": 10
    }

    # Use httpx.AsyncClient to make a non-blocking request
    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL, params=params)
        
        # Check if the external API request was successful
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Failed to fetch jobs from external API")
            
        data = response.json()

    # Parse and clean up the results before sending them back [cite: 1028-1029]
    jobs_list = []
    for job in data.get("results", []):
        jobs_list.append({
            "id": job.get("id"),
            "title": job.get("title"),
            "company": job.get("company", {}).get("display_name"),
            "location": job.get("location", {}).get("display_name"),
            "description": job.get("description"),
            "url": job.get("redirect_url")
        })

    return {"total_found": len(jobs_list), "jobs": jobs_list}