
from pathlib import Path
import pymupdf
from document_processor import chunk_text

pdf_path = Path("sample_docs/sample_empty.txt")

if not pdf_path.exists():
    print(f"PDF not found: {pdf_path}")
    raise SystemExit(1)

with pymupdf.open(pdf_path) as doc:
    page_count = len(doc)
    text = "\n".join(page.get_text() for page in doc)

print("PDF pages:", page_count)
print("Extracted text length:", len(text))
print("\nExtracted text preview:")
print(text[:500])

if not text.strip():
    print("\nNo text found. The PDF may be scanned.")
    raise SystemExit(1)

chunks = chunk_text(text, chunk_size=500, overlap=100)

print("\nTotal chunks:", len(chunks))
for i, chunk in enumerate(chunks[:3], start=1):
    print(f"\nChunk {i} — {len(chunk.split())} words")
    print(chunk[:200])

print("\nPDF extraction and chunking test passed!")
