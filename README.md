# HORIZON AI Core

Central API foundation for the HORIZON AI agent ecosystem.

## Endpoints

- `GET /` — service status
- `GET /health` — health check for hosting platforms
- `/docs` — interactive API documentation

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

## Deploy

The repository includes `render.yaml` for deployment on Render. Configure `CORS_ORIGINS` with the exact origins that are allowed to call the API. Do not commit secrets or private keys.

## Security status

This is an initial health/API foundation. It is not yet an authenticated agent gateway. Do not expose privileged agent operations until authentication, authorization, request limits, and audit logging are implemented.
