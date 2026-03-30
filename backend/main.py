import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes.upload import router as upload_router
from api.routes.query import router as query_router

app = FastAPI(title="Smart Doc Intelligence — CA & Indian Policy Docs")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router, prefix="/api")
app.include_router(query_router, prefix="/api")

@app.get("/")
def root():
    return {"status": "ok", "message": "Smart Doc Intelligence API"}

@app.get("/health")
def health():
    return {"status": "ok"}