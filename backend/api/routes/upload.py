import uuid, os, shutil
from fastapi import APIRouter, UploadFile, File
from core.parser import extract_text
from core.chunker import chunk_text
from core.vectorstore import add_chunks
from api.models import UploadResponse
from db.mongo import save_session

router = APIRouter()
UPLOAD_DIR = "/tmp/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload", response_model=UploadResponse)
async def upload_file(file: UploadFile = File(...)):
    session_id = str(uuid.uuid4())
    file_path = f"{UPLOAD_DIR}/{session_id}_{file.filename}"
    
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    
    text = extract_text(file_path)
    chunks = chunk_text(text, source_name=file.filename)
    add_chunks(session_id, chunks)
    
    await save_session(session_id, file.filename, len(chunks))
    
    return UploadResponse(
        session_id=session_id,
        filename=file.filename,
        chunks_indexed=len(chunks),
        message=f"Successfully indexed {len(chunks)} chunks"
    )