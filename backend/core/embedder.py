import requests
import os

HF_TOKEN = os.environ.get("HF_TOKEN", "")
EMBED_MODEL = os.environ.get("EMBED_MODEL", "sentence-transformers/all-MiniLM-L6-v2")

API_URL = f"https://router.huggingface.co/hf-inference/models/{EMBED_MODEL}/pipeline/feature-extraction"
HEADERS = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}

def _get_embeddings(texts: list[str]) -> list[list[float]]:
    response = requests.post(
        API_URL,
        headers=HEADERS,
        json={"inputs": texts}
    )
    if response.status_code != 200:
        raise ValueError(f"HF API error {response.status_code}: {response.text}")
    result = response.json()
    if isinstance(result, dict) and "error" in result:
        raise ValueError(f"HuggingFace API error: {result['error']}")
    if isinstance(result, list) and len(result) > 0:
        if isinstance(result[0], list) and len(result[0]) > 0 and isinstance(result[0][0], list):
            result = [r[0] for r in result]
    return result

def get_embedder():
    class APIEmbedder:
        def embed_documents(self, texts):
            return _get_embeddings(texts)
        def embed_query(self, text):
            return _get_embeddings([text])[0]
    return APIEmbedder()

