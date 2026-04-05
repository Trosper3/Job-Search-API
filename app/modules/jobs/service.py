import httpx
import os
from fastapi import HTTPException

ADZUNA_APP_ID = "ID_GOES_HERE"
ADZUNA_APP_KEY = "KEY_GOES_HERE"
BASE_URL = "https://api.adzuna.com/v1/api/jobs/gb/search/1"

async def fetch_jobs(query: str):

    params = {
        "app_id": ADZUNA_APP_ID,
        "app_key": ADZUNA_APP_KEY,
        "results_per_page": 10,
        "what": query
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL, params=params)

        # Check if the request was successful
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Error fetching jobs from Adzuna API")
        
        data = response.json()

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

        return {"Total_found": len(jobs_list), "jobs": jobs_list}