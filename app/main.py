from fastapi import FastAPI
from app.modules.jobs.routes import router as jobs_router

app = FastAPI(title = "Job Search API",
              description="CS 3321 Project - Job Search API",
              version="1.0.0")

# Include the jobs router
app.include_router(jobs_router, prefix="/jobs", tags=["jobs"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Job Search API!"}