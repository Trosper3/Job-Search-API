from fastapi import FastAPI
from app.modules.analyze.routes import router as analyze_router
from app.modules.jobs.routes import router as jobs_router
from app.modules.stats.routes import router as stats_router

app = FastAPI(title = "Job Search API",
              description="CS 3321 Project - Job Search API",
              version="1.0.0")

# Include the jobs router
app.include_router(stats_router, prefix="/stats", tags=["stats"])
app.include_router(jobs_router, prefix="/jobs", tags=["jobs"])
app.include_router(analyze_router, prefix="/analyze", tags=["analyze"])
app.include_router(stats_router, prefix="/stats", tags=["stats"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Job Search API!"}