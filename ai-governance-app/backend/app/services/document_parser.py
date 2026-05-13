import os
import aiofiles
from pathlib import Path
from fastapi import UploadFile
from pypdf import PdfReader
from docx import Document as DocxDocument
from app.core.config import settings


SUPPORTED_TYPES = {
    "application/pdf": ".pdf",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document": ".docx",
    "text/plain": ".txt",
    "text/markdown": ".md",
}


async def save_upload(file: UploadFile, project_id: str) -> str:
    upload_path = Path(settings.upload_dir) / project_id
    upload_path.mkdir(parents=True, exist_ok=True)
    dest = upload_path / file.filename
    async with aiofiles.open(dest, "wb") as out:
        content = await file.read()
        await out.write(content)
    return str(dest)


def extract_text(file_path: str) -> str:
    path = Path(file_path)
    suffix = path.suffix.lower()

    if suffix == ".pdf":
        return _extract_pdf(file_path)
    elif suffix == ".docx":
        return _extract_docx(file_path)
    elif suffix in (".txt", ".md"):
        return path.read_text(encoding="utf-8", errors="replace")
    else:
        raise ValueError(f"Unsupported file type: {suffix}")


def _extract_pdf(path: str) -> str:
    reader = PdfReader(path)
    parts = []
    for page in reader.pages:
        text = page.extract_text()
        if text:
            parts.append(text)
    return "\n\n".join(parts)


def _extract_docx(path: str) -> str:
    doc = DocxDocument(path)
    paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
    return "\n\n".join(paragraphs)


def chunk_text(text: str, max_chars: int = 6000, overlap: int = 400) -> list[str]:
    """Split text into overlapping chunks for LLM context windows."""
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + max_chars, len(text))
        chunks.append(text[start:end])
        if end == len(text):
            break
        start = end - overlap
    return chunks
