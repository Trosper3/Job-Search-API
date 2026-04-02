# Docker Setup for Job Searcher API

To run this application locally using Docker, ensure you have Docker Desktop installed and running.

### 1. Build the Docker Image
Run this command from the root of the project to build the image:
`docker build -t job-searcher-api .`

### 2. Run the Container
Once built, start the container and map it to port 8000:
`docker run -d -p 8000:8000 job-searcher-api`

The API will now be accessible at http://localhost:8000