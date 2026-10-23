
import hashlib

import streamlit as st
from dotenv import load_dotenv

from document_processor import extract_text, chunk_text
from rag_pipeline import create_vector_store, answer_question

load_dotenv()

st.set_page_config(
    page_title="StudyMate AI - Document Q&A",
    page_icon="📚",
    layout="wide",
)

st.title("📚 StudyMate AI")
st.subheader("Ask questions from your documents")
st.write(
    "Upload a PDF or TXT file and ask questions "
    "based on its content."
)

uploaded_file = st.file_uploader(
    "Upload your document",
    type=["pdf", "txt"],
)

for key, default in {
    "index": None,
    "chunks": None,
    "document_id": None,
    "filename": None,
    "messages": [],
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

if uploaded_file is not None:
    document_bytes = uploaded_file.getvalue()
    document_id = hashlib.sha256(document_bytes).hexdigest()
    if st.session_state.document_id != document_id:
        # Drop the previous document before processing, so a failed upload
        # cannot leave the old index available under the new filename.
        st.session_state.index = None
        st.session_state.chunks = None
        st.session_state.document_id = None
        st.session_state.filename = None
        st.session_state.messages = []
        with st.spinner("Reading and processing document..."):
            try:
                uploaded_file.seek(0)
                text = extract_text(uploaded_file)

                if not text.strip():
                    st.error("No readable text found in this document.")
                    st.stop()

                chunks = chunk_text(
                    text,
                    chunk_size=500,
                    overlap=100,
                )

                index, chunks = create_vector_store(chunks)

                st.session_state.index = index
                st.session_state.chunks = chunks
                st.session_state.document_id = document_id
                st.session_state.filename = uploaded_file.name
                st.session_state.messages = []

                st.success(
                    f"Document processed! "
                    f"{len(chunks)} chunks created."
                )

            except Exception as e:
                st.error(f"Document processing failed: {e}")
                st.stop()

    st.caption(f"Current document: {uploaded_file.name}")

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            if message.get("sources"):
                with st.expander("Retrieved source context"):
                    for source in message["sources"]:
                        st.markdown(
                            f"**Chunk {source['chunk_number']}** "
                            f"(similarity: {source['score']:.2f})"
                        )
                        st.write(source["text"])

    question = st.chat_input("Ask a question about your document")

    if question:
        if not question.strip():
            st.warning("Please enter a question about the uploaded document.")
            st.stop()
        st.session_state.messages.append(
            {"role": "user", "content": question}
        )

        with st.chat_message("user"):
            st.markdown(question)

        with st.chat_message("assistant"):
            with st.spinner("Finding information and generating answer..."):
                try:
                    answer = answer_question(
                        question,
                        st.session_state.index,
                        st.session_state.chunks,
                    )
                    st.markdown(answer["answer"])
                    with st.expander("Retrieved source context"):
                        for source in answer["sources"]:
                            st.markdown(
                                f"**Chunk {source['chunk_number']}** "
                                f"(similarity: {source['score']:.2f})"
                            )
                            st.write(source["text"])

                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": answer["answer"],
                            "sources": answer["sources"],
                        }
                    )

                except Exception as e:
                    st.error(f"Could not generate an answer: {e}")

else:
    if st.session_state.document_id is not None:
        st.session_state.index = None
        st.session_state.chunks = None
        st.session_state.document_id = None
        st.session_state.filename = None
        st.session_state.messages = []
    st.info("Upload a PDF or TXT document to get started.")
