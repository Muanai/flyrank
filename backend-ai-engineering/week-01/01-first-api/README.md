# 01 — Build Your First API Endpoint

A minimal FastAPI application demonstrating the HTTP request-response cycle and JSON payloads.

## Requirements

- Python 3.11+
- uv

## Local Setup

```bash
uv sync
```
## Execution

```bash
uvicorn app:app --reload
```

## Endpoints

- `GET /`
- `GET /health`

## Verification

```bash
curl http://127.0.0.1:8000/
curl http://127.0.0.1:8000/health
```