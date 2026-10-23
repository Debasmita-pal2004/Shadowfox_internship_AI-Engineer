
import pymupdf


def extract_text(uploaded_file):
    """Extract text from an uploaded PDF or TXT file."""
    filename = uploaded_file.name.lower()

    if filename.endswith(".pdf"):
        text_parts = []

        with pymupdf.open(
             stream=uploaded_file.getvalue(),
             filetype="pdf"
        ) as pdf:
            for page in pdf:
                text_parts.append(page.get_text("text"))

        text = "\n".join(text_parts)

    elif filename.endswith(".txt"):
        text = uploaded_file.getvalue().decode("utf-8-sig")

    else:
        raise ValueError("Only PDF and TXT files are supported.")

    if not text.strip():
        raise ValueError(
            f"No readable text found in {uploaded_file.name}. "
            "The PDF may be scanned and require OCR."
        )

    return text


def chunk_text(text, chunk_size=500, overlap=100):
    """Split text into overlapping chunks measured in words."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive.")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError(
            "overlap must be non-negative and smaller than chunk_size."
        )

    words = text.split()
    chunks = []
    start = 0

    while start < len(words):
        end = min(start + chunk_size, len(words))
        chunk = " ".join(words[start:end])

        if chunk.strip():
            chunks.append(chunk)

        if end == len(words):
            break

        start = end - overlap

    return chunks
