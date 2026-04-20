# Job Search API

A backend-only job search system built with FastAPI.  
This project demonstrates production-style backend engineering including API design, third-party integration, Docker containerization, CI/CD pipelines, automated testing, and secure secrets management.

---

## 📌 Project Goal

The goal of this project is not feature complexity, but **engineering delivery**:

- Backend API development
- Integration with external job search API
- Fully containerized deployment
- Automated testing with coverage enforcement
- CI/CD pipeline using GitHub Actions
- Secure secrets management using Doppler
- Cloud deployment on AWS

---

## 🧱 Tech Stack

- Python 3.11+
- FastAPI
- Uvicorn
- HTTPX (third-party API calls)
- Pytest
- Coverage.py
- Docker
- UV (package manager)
- GitHub Actions (CI/CD)
- Doppler (secrets management)
- AWS EC2 (deployment target)

---

## 🚀 Running Locally (Development)

### 1. Clone repository

```bash
git clone <repo-url>
cd Job-Search-API
```

### 2. Create virtual environment (UV)
```bash
uv venv
```

#### 1. Windows
```bash
.venv\Scripts\Activate
```

#### 2. MacOS/Linux
```bash
source .venv/bin/activate
```

### 3. Install dependencies (DEV MODE)
```bash
uv sync --dev
```

### 4. Run API locally (development mode)
```bash
uvicorn main:app --reload
```

### 5. Open Swagger UI
```bash
http://127.0.0.1:8000/docs
```

### 6. Development Tools

#### 1. Coverage
```bash
coverage run --source=app -m pytest
coverage report
```

#### 2. Docker
```bash
docker build -t job-search-api .
```

```bash
docker run -p 8000:8000 job-search-api
```
