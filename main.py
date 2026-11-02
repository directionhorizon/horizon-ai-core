import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="HORIZON AI Core",
    description="Central API foundation for the HORIZON AI agent ecosystem.",
    version="0.1.0",
)

origins = [origin.strip() for origin in os.getenv("CORS_ORIGINS", "").split(",") if origin.strip()]
if origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=False,
        allow_methods=["GET"],
        allow_headers=["Authorization", "Content-Type"],
    )

@app.get("/")
async def root():
    return {"service": "HORIZON AI Core", "status": "online", "version": "0.1.0"}

@app.get("/health")
async def health():
    return {"status": "healthy"}
