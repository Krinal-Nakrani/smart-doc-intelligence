from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes.upload import router as upload_router
from api.routes.query import router as query_router

app = FastAPI(title="Smart Doc Intelligence — CA & Indian Policy Docs")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # tighten this after deployment
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router, prefix="/api")
app.include_router(query_router, prefix="/api")

@app.get("/health")
def health():
    return {"status": "ok"}
