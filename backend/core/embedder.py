# Swap: your Colab used HuggingFaceEmbeddings — keeping same model, no GPU needed locally
from langchain_community.embeddings import HuggingFaceEmbeddings
from config import EMBED_MODEL

_embedder = None

def get_embedder():
    global _embedder
    if _embedder is None:
        _embedder = HuggingFaceEmbeddings(
            model_name=EMBED_MODEL,
            model_kwargs={"device": "cpu"}   # Railway has no GPU; cpu is fine for MiniLM
        )
    return _embedder