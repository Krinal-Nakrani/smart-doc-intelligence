import chromadb
from config import CHROMA_PATH
from core.embedder import get_embedder

client = chromadb.PersistentClient(path=CHROMA_PATH)

def get_or_create_collection(session_id: str):
    return client.get_or_create_collection(name=f"session_{session_id}")

def add_chunks(session_id: str, chunks: list[dict]):
    collection = get_or_create_collection(session_id)
    embedder = get_embedder()
    texts = [c["text"] for c in chunks]
    embeddings = embedder.embed_documents(texts)
    collection.add(
        ids=[c["chunk_id"] for c in chunks],
        embeddings=embeddings,
        documents=texts,
        metadatas=[{"source": c["source"]} for c in chunks]
    )

def similarity_search(session_id: str, query: str, top_k: int = 4):
    collection = get_or_create_collection(session_id)
    embedder = get_embedder()
    q_embedding = embedder.embed_query(query)
    results = collection.query(
        query_embeddings=[q_embedding],
        n_results=top_k
    )
    hits = []
    for i, doc in enumerate(results["documents"][0]):
        hits.append({
            "text": doc,
            "source": results["metadatas"][0][i]["source"],
            "score": 1 - results["distances"][0][i]
        })
    return hits