import os
import secrets

from fastapi import Depends, FastAPI, Header, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="HORIZON AI Core",
    description="Central API foundation for the HORIZON AI agent ecosystem.",
    version="0.2.0",
)

origins = [origin.strip() for origin in os.getenv("CORS_ORIGINS", "").split(",") if origin.strip()]
if origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=False,
        allow_methods=["GET"],
        allow_headers=["Authorization", "Content-Type", "X-API-Key"],
    )


def require_api_key(x_api_key: str | None = Header(default=None)):
    expected_key = os.getenv("HORIZON_API_KEY")
    if not expected_key:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="API authentication is not configured",
        )
    if not x_api_key or not secrets.compare_digest(x_api_key, expected_key):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key",
        )


@app.get("/")
async def root():
    return {"service": "HORIZON AI Core", "status": "online", "version": "0.2.0"}


@app.get("/health")
async def health():
    return {"status": "healthy"}


@app.get("/api/status", dependencies=[Depends(require_api_key)])
async def api_status():
    return {"service": "HORIZON AI Core", "authenticated": True, "status": "ready"}
