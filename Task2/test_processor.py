
from document_processor import chunk_text

text = " ".join(
    f"word{i}" for i in range(1200)
)

chunks = chunk_text(
    text,
    chunk_size=500,
    overlap=100
)

print("Total chunks:", len(chunks))
print("First chunk word count:", len(chunks[0].split()))
print("Second chunk word count:", len(chunks[1].split()))

# Check that overlapping words are preserved.
assert chunks[0].split()[-100:] == chunks[1].split()[:100]

print("Chunking test passed!")
