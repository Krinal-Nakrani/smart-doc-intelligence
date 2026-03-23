from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI
from datetime import datetime

client = AsyncIOMotorClient(MONGO_URI)
db = client["smart_doc_intelligence"]

async def save_session(session_id: str, filename: str, chunks: int):
    await db.sessions.insert_one({
        "session_id": session_id,
        "filename": filename,
        "chunks": chunks,
        "created_at": datetime.utcnow()
    })