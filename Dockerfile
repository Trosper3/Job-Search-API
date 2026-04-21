FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

ARG PROJECT_URL=https://github.com/Trosper3/Job-Search-API
ARG PROJECT_BRANCH=main

ENV PATH="/tmp/Job-Search-API/.venv/bin:$PATH"
ENV UV_PROJECT_ENVIRONMENT=/tmp/Job-Search-API/.venv

RUN apt-get update \
  && apt-get install -y --no-install-recommends --no-install-suggests \
    curl \
    git \
    bash \
    gnupg \
  && ln -sf /bin/bash /bin/sh \
  && curl -Ls --tlsv1.2 --proto "=https" --retry 3 https://cli.doppler.com/install.sh | sh \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /tmp
RUN git clone $PROJECT_URL
WORKDIR /tmp/Job-Search-API

RUN git switch $PROJECT_BRANCH \
  && uv sync --frozen

EXPOSE 8000

CMD ["doppler", "run", "--", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]