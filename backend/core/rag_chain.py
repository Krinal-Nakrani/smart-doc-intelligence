from groq import Groq
from config import GROQ_API_KEY, GROQ_MODEL
from core.vectorstore import similarity_search

client = Groq(api_key=GROQ_API_KEY)

SYSTEM_PROMPT = """You are an expert assistant for Indian government policy documents and CA exam papers.
Answer ONLY based on the provided context. If the answer is not in the context, say so clearly.
Be concise and cite the source document."""

def answer_query(session_id: str, question: str, top_k: int = 4) -> dict:
    hits = similarity_search(session_id, question, top_k=top_k)
    
    context_str = "\n\n---\n\n".join(
        [f"[Source: {h['source']}]\n{h['text']}" for h in hits]
    )
    
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"Context:\n{context_str}\n\nQuestion: {question}"}
    ]
    
    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=messages,
        max_tokens=512,
        temperature=0.2
    )
    
    return {
        "answer": response.choices[0].message.content,
        "sources": hits
    }