import PyPDF2
import docx
from pathlib import Path

def extract_text(file_path: str) -> str:
    ext = Path(file_path).suffix.lower()
    
    if ext == ".pdf":
        text = ""
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() or ""
        return text
    
    elif ext == ".docx":
        doc = docx.Document(file_path)
        return "\n".join([p.text for p in doc.paragraphs])
    
    elif ext == ".txt":
        return Path(file_path).read_text(encoding="utf-8")
    
    else:
        raise ValueError(f"Unsupported file type: {ext}")