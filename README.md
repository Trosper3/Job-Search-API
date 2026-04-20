# Job-Search-API

A FastAPI backend for searching jobs through the Adzuna API, analyzing job descriptions, and summarizing job-market statistics. The project is organized around production-style backend delivery: external API integration, automated testing, Docker support, and secrets handled through Doppler.

## Overview

The application exposes four HTTP endpoints:

- `GET /` returns a simple welcome message
- `GET /jobs?q=python` fetches jobs from Adzuna
- `GET /stats?q=python` calculates summary statistics from Adzuna results
- `POST /analyze` extracts keywords from a job description

The codebase is built with FastAPI, HTTPX, and Uvicorn, and the project dependencies are managed with UV through `pyproject.toml`.

## Requirements

- Python 3.12+
- UV
- Docker Desktop, if you want to run the app in a container
- Doppler workspace: `ISU - CS3321`
- Doppler project: `team-1`
- Doppler config: `dev`
- Adzuna secrets stored in Doppler:
	- `ADZUNA_APP_ID`
	- `ADZUNA_APP_KEY`

For the presentation, use Doppler so you never have to type the secret values into the terminal.

## Local Setup

### 1. Clone the repository

```bash
git clone <repo-url>
cd Job-Search-API
```

### 2. Create a virtual environment

```bash
uv venv
```

### 3. Activate the environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
uv sync --dev
```

### 5. Use Doppler secrets

Load the Adzuna credentials into the Doppler workspace `ISU - CS3321`, project `team-1`, config `dev`. The application reads `ADZUNA_APP_ID` and `ADZUNA_APP_KEY` from the environment, and Doppler injects them at runtime.

## Run the Application

Start the API with Uvicorn:

```bash
uv run uvicorn app.main:app --reload
```

Presentation-friendly option with Doppler:

```bash
doppler run --project "team-1" --config dev -- uv run uvicorn app.main:app --reload
```

The API will be available at:

- http://127.0.0.1:8000
- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/redoc

## API Endpoints

### `GET /`

Returns a basic welcome response.

### `GET /jobs?q=keyword`

Fetches job postings from Adzuna using the `q` query parameter.

Example:

```bash
curl "http://127.0.0.1:8000/jobs?q=python"
```

### `GET /stats?q=keyword`

Fetches job data from Adzuna and returns summary statistics such as total jobs, remote jobs, top companies, and top locations.

Example:

```bash
curl "http://127.0.0.1:8000/stats?q=python"
```

### `POST /analyze`

Analyzes a job description and extracts keywords.

Example:

```bash
curl -X POST "http://127.0.0.1:8000/analyze" \
	-H "Content-Type: application/json" \
	-d '{"description":"Python developer with FastAPI and Docker experience"}'
```

## Testing

Run the test suite with Pytest:

```bash
pytest
```

Run tests with coverage:

```bash
coverage run --source=app -m pytest
coverage report
```

The repo includes unit tests for the FastAPI routes and service logic, including mocked Adzuna responses.

## Docker

The included Dockerfile currently installs from `requirements.txt`, so the container workflow matches the committed Docker setup. Local development still uses UV and `pyproject.toml`.

Build the image:

```bash
docker build -t job-search-api .
```

Run the container:

```bash
docker run -p 8000:8000 \
	job-search-api
```

For a presentation, run the container through Doppler so the secrets are injected automatically instead of being typed into the terminal:

```bash
doppler run --project "team-1" --config dev -- docker run -p 8000:8000 job-search-api
```

## Project Structure

```text
Job-Search-API/
├── app/
│   ├── main.py
│   ├── modules/
│   │   ├── analyze/
│   │   ├── health/
│   │   ├── jobs/
│   │   └── stats/
│   └── tests/
├── pyproject.toml
├── requirements.txt
├── Dockerfile
├── DOCKER_SETUP.md
└── README.md
```

## Notes

- The application uses environment variables for Adzuna credentials at runtime, and Doppler is the preferred source for the `dev` config.
- GitHub Actions also needs a Doppler service token stored as a GitHub secret so it can read `ISU - CS3321` / `team-1` / `dev` during CI.
- The `health` module currently exists in the project structure, but the active routes exposed by `app.main` are `/`, `/jobs`, `/stats`, and `/analyze`.
- The codebase targets Python 3.12 and uses `uv` for dependency management.
