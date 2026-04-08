# 📚 Smart Doc Intelligence

> RAG-powered document Q&A — built specifically for **CA Exam Papers** and **Indian Government Policy Documents**

## Tech Stack
- **Backend**: FastAPI + LangChain + ChromaDB + Groq (Llama 3.3 70B)
- **Embeddings**: HuggingFace all-MiniLM-L6-v2
- **Database**: MongoDB Atlas (session storage)
- **Frontend**: React + Vite → deployed on Vercel
- **Backend Hosting**: Render

## Features
- Upload PDF, DOCX, or TXT documents
- Automatic text extraction, chunking & embedding
- Semantic similarity search via ChromaDB
- Grounded answers with source paragraph highlights
- Session-based document management

## Local Setup

### Backend
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload --port 8000

### Frontend
cd frontend
npm install
npm run dev

## Environment Variables
GROQ_API_KEY
<<<<<<< HEAD

HF_TOKEN

MONGO_URI

EMBED_MODEL
=======
HF_TOKEN
MONGO_URI
EMBED_MODEL
>>>>>>> 8bd4df1 (final touch and deployment)
