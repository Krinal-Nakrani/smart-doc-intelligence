# 📚 Smart Doc Intelligence

> RAG-powered document Q&A — built specifically for **CA Exam Papers** and **Indian Government Policy Documents**

## Tech Stack
- **Backend**: FastAPI + LangChain + ChromaDB + Groq (Llama 3.3 70B)
- **Embeddings**: HuggingFace all-MiniLM-L6-v2
- **Database**: MongoDB Atlas (session storage)
- **Frontend**: React + Vite → deployed on Vercel
- **Backend Hosting**: Railway

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
GROQ_API_KEY=
HF_TOKEN=
MONGO_URI=
```

---

Now you have **every single file complete**. Here's your exact next steps sequence:
```
1. Fill in your real keys in .env
2. cd backend → activate venv → pip install -r requirements.txt
3. uvicorn main:app --reload --port 8000   ← test backend at localhost:8000/docs
4. cd frontend → npm run dev               ← test frontend at localhost:5173
5. git init → push to GitHub → deploy backend on Railway → frontend on Vercel