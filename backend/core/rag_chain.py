from groq import Groq
import os

GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")
GROQ_MODEL = "llama-3.3-70b-versatile"

from core.vectorstore import similarity_search

client = Groq(api_key=GROQ_API_KEY)

SYSTEM_PROMPT = """You are a helpful document assistant. 
The user has uploaded a document and you must answer questions based ONLY on the context chunks provided below.
If the context contains relevant information, use it to answer.
If the context is empty or irrelevant, say: "I could not find relevant information in the uploaded document."
Never say "no context provided" — always try to use what is given."""

def answer_query(session_id: str, question: str, top_k: int = 4) -> dict:
    hits = similarity_search(session_id, question, top_k=top_k)
    
    if not hits:
        return {
            "answer": "No relevant content found in the document. Please try a different question.",
            "sources": []
        }
    
    context_str = "\n\n---\n\n".join(
        [f"[Source: {h['source']}]\n{h['text']}" for h in hits]
    )
    
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"Context from uploaded document:\n{context_str}\n\nQuestion: {question}"}
    ]
    
    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=messages,
        max_tokens=512,
        temperature=0
    )
    
    return {
        "answer": response.choices[0].message.content,
        "sources": hits
    }

# from groq import Groq
# from config import GROQ_API_KEY, GROQ_MODEL
# from core.vectorstore import similarity_search

# client = Groq(api_key=GROQ_API_KEY)

# SYSTEM_PROMPT = """You are an expert assistant for Indian government policy documents and CA exam papers.
# Answer ONLY based on the provided context. If the answer is not in the context, say so clearly.
# Be concise and cite the source document."""

# def answer_query(session_id: str, question: str, top_k: int = 4) -> dict:
#     hits = similarity_search(session_id, question, top_k=top_k)
    
#     context_str = "\n\n---\n\n".join(
#         [f"[Source: {h['source']}]\n{h['text']}" for h in hits]
#     )
    
#     messages = [
#         {"role": "system", "content": SYSTEM_PROMPT},
#         {"role": "user", "content": f"Context:\n{context_str}\n\nQuestion: {question}"}
#     ]
    
#     response = client.chat.completions.create(
#         model=GROQ_MODEL,
#         messages=messages,
#         max_tokens=512,
#         temperature=0.2
#     )
    
#     return {
#         "answer": response.choices[0].message.content,
#         "sources": hits
#     }