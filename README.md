# Job Search API

A modular, asynchronously driven FastAPI application designed to query live labor market data, calculate business statistics, and extract analytical insights from real-time job listings. This system functions as a robust middleware tier connecting upstream clients with live data providers.

## Project Architecture & Tech Stack

This application utilizes a clean separation of concerns, separating routing interfaces from underlying business and computational services.

* **Framework:** FastAPI (Asynchronous Python Web Framework)
* **Data Aggregation Engine:** Adzuna API Integration
* **Package Management:** [uv](https://docs.astral.sh/uv/)
* **Testing Infrastructure:** Pytest framework with full unit and integration test coverage

```
├── app/
│   ├── main.py                     # API Gateway / Application Entrypoint
│   ├── modules/
│   │   ├── jobs/                   # Live job ingestion service
│   │   │   ├── routes.py
│   │   │   └── service.py
│   │   ├── stats/                  # Quantitative calculations engine
│   │   │   ├── routes.py
│   │   │   └── service.py
│   │   └── analyze/                # Qualitative skill extraction module
│   │       ├── routes.py
│   │       └── service.py
│   └── tests/                      # Unit & integration testing suites
├── pyproject.toml                  # Project metadata & dependencies
├── Dockerfile                      # Container build definition
└── DOCKER_SETUP.md                 # Docker usage reference
```

---

## Key Features & Core Modules

### 1. Ingestion Engine (`/jobs`)
Handles live data retrieval directly from third-party talent market systems (Adzuna). It serves clean JSON responses representing current employment postings mapped by specific programmatic keywords or job titles.

### 2. Quantitative Math Engine (`/stats`)
Interceptors evaluate real-time listings to perform statistical calculations. Rather than returning raw unparsed strings, this module delivers quantitative market calculations (e.g., salary ranges, distributions, and posting volumes) to supply downstream applications with business insights.

### 3. Qualitative Analytics Engine (`/analyze`)
Implements parsing algorithms to scan live job descriptions. It programmatically isolates and counts frequency metrics for industry-sought tech skills, converting dense prose into actionable career trend data.

---

## Local Development & Setup

### 1. Prerequisites
Ensure you have Python 3.12+ and [uv](https://docs.astral.sh/uv/getting-started/installation/) installed.

### 2. Install Dependencies
Navigate to the root directory and sync the project's dependencies (this creates a virtual environment automatically):

```bash
uv sync
```

### 3. Configure Environment Variables
The application requires Adzuna API credentials to fetch live job data. Create a `.env` file in the project root:

```bash
ADZUNA_APP_ID=your_app_id
ADZUNA_APP_KEY=your_app_key
```

### 4. Execution (Running the Server)
Launch the asynchronous development server using uvicorn:

```bash
uv run uvicorn app.main:app --reload
```

Once the worker process initializes, the server will sit at `http://127.0.0.1:8000`.

### Interactive API Documentation
FastAPI natively exposes OpenAPI documentation strings. While the application server is active, navigate to either of the following endpoints to evaluate, interact with, or test live query parameters:

* **Swagger Interactive UI:** `http://127.0.0.1:8000/docs`
* **ReDoc Alternative UI:** `http://127.0.0.1:8000/redoc`

### Primary Endpoint Mappings

| Endpoint | Description |
|---|---|
| `GET /jobs?q={keyword}` | Ingests active listings matching specified keywords. |
| `GET /stats?q={keyword}` | Aggregates listings and computes quantitative market statistics. |
| `GET /analyze?q={keyword}` | Runs token frequency extraction to surface major tech skills required in current postings. |

---

## Testing

The repository features comprehensive unit and integration tests inside the `app/tests/` module. To verify route statuses, endpoint assertions, and mathematical parsing logic locally, run:

```bash
uv run pytest
```

---

## Docker

See [DOCKER_SETUP.md](DOCKER_SETUP.md) for building and running the application in a container.

---

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
