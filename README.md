# Job-Search-API

## GitHub Actions CI/CD

This repository uses a 4-job GitHub Actions workflow in `.github/workflows/pipeline.yml`.

1. **Test**: installs dependencies, runs unit tests, and enforces at least 80% coverage.
2. **Quality Gates**: runs linting with Ruff and validates Adzuna credentials against the live API (on non-PR events).
3. **Build and Push**: builds the Docker image and pushes tags (`latest` and commit SHA) to Docker Hub.
4. **Deploy**: connects to an EC2 host over SSH, pulls the latest Docker image from Docker Hub, and runs the container.

### Required GitHub Repository Secrets

- `DOPPLER_SERVICE_TOKEN`

### Required Doppler Secrets

- `DOCKER_USERNAME`
- `DOCKER_PASSWORD`
- `ADZUNA_APP_ID`
- `ADZUNA_APP_KEY`
- `AWS_IP`
- `AWS_EC2_USERNAME`
- `SSH_AWS_PEM`
- `AWS_EC2_PORT` (optional; defaults to `22` in workflow)

### AWS Host Prerequisites

- Docker must be installed on the target EC2 instance.
- The EC2 security group should allow inbound traffic on port `8000`.
- The SSH user must have permission to run Docker commands.
