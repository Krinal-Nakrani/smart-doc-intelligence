from pydantic import BaseModel

class QueryRequest(BaseModel):
    session_id: str
    question: str
    top_k: int = 4

class QueryResponse(BaseModel):
    answer: str
    sources: list[dict]

class UploadResponse(BaseModel):
    session_id: str
    filename: str
    chunks_indexed: int
    message: str