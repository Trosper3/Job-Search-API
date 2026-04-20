# Docker Setup for Job Searcher API

To run this application locally using Docker, ensure you have Docker Desktop installed and running.

If you have the Adzuna secrets stored in Doppler, use the `ISU - CS3321` workspace, `team-1` project, and `dev` config so the container starts without manual secret entry.

### 1. Build the Docker Image
Run this command from the root of the project to build the image:
`docker build -t job-search-api .`

### 2. Run the Container
Once built, start the container and map it to port 8000:
`docker run -p 8000:8000 job-search-api`

If you are using Doppler, run the container through Doppler instead:
`doppler run --project "team-1" --config dev -- docker run -p 8000:8000 job-search-api`

The API will now be accessible at http://localhost:8000