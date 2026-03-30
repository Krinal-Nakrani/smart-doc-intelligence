from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import CHUNK_SIZE, CHUNK_OVERLAP

def chunk_text(text: str, source_name: str) -> list[dict]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100,
        separators=["\n\n", "\n", ".", " "]
    )
    chunks = splitter.split_text(text)
    # Limit to 100 chunks max to avoid memory issues
    chunks = chunks[:100]
    return [
        {"text": chunk, "source": source_name, "chunk_id": f"{source_name}_{i}"}
        for i, chunk in enumerate(chunks)
    ]