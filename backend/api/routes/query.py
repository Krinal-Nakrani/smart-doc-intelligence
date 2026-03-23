from fastapi import APIRouter
from api.models import QueryRequest, QueryResponse
from core.rag_chain import answer_query

router = APIRouter()

@router.post("/query", response_model=QueryResponse)
async def query_document(req: QueryRequest):
    result = answer_query(req.session_id, req.question, req.top_k)
    return QueryResponse(**result)