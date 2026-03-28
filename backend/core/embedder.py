import requests
from config import HF_TOKEN, EMBED_MODEL

API_URL = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{EMBED_MODEL}"
HEADERS = {"Authorization": f"Bearer {HF_TOKEN}"}

def _get_embeddings(texts: list[str]) -> list[list[float]]:
    response = requests.post(
        API_URL,
        headers=HEADERS,
        json={"inputs": texts, "options": {"wait_for_model": True}}
    )
    return response.json()

def get_embedder():
    class APIEmbedder:
        def embed_documents(self, texts):
            return _get_embeddings(texts)
        def embed_query(self, text):
            return _get_embeddings([text])[0]
    return APIEmbedder()
