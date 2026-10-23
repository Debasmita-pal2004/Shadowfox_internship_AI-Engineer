# 📚 StudyMate AI — Intermediate Level

## Project Overview

StudyMate AI is a document-based Question Answering Assistant that allows users to upload PDF or TXT files and ask questions about their content. It uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from uploaded documents and generate context-based answers using Google's Gemini API.

## Features

- **PDF and TXT Upload:** Upload documents for question answering.
- **Text Extraction:** Extract text from PDF and TXT files.
- **Text Chunking:** Split extracted text into smaller, overlapping chunks.
- **Text Embeddings:** Generate semantic embeddings using Sentence Transformers.
- **Vector Search:** Use FAISS to retrieve relevant document chunks.
- **AI-Powered Answers:** Generate answers using the Gemini API based on retrieved document context.
- **Error Handling:** Handle empty questions, unreadable documents, and API errors.
- **Interactive Interface:** Use a simple interface built with Streamlit.

## Technologies Used

- Python
- Streamlit
- PyMuPDF
- Sentence Transformers
- FAISS
- Google Gemini API
- python-dotenv
- NumPy

## How It Works

1. The user uploads a PDF or TXT document.
2. The application extracts the document text.
3. The extracted text is divided into overlapping chunks.
4. Sentence Transformers converts the chunks into embeddings.
5. FAISS stores the embeddings and retrieves the most relevant chunks for a question.
6. The retrieved text is passed to the Gemini API as context.
7. Gemini generates an answer based on the provided document content.
8. The answer is displayed in the Streamlit interface.

## Project Structure

```text
Task2/
├── app.py
├── document_processor.py
├── rag_pipeline.py
├── requirements.txt
├── test_processor.py
├── .env
└── sample_docs/
```

**Note:** The `.env` file contains the API key and must not be uploaded to GitHub. The `sample_docs/` folder may contain local test documents and can be excluded from version control.

## Installation and Setup

### 1. Clone or download the project

Open a terminal in the `Task2` directory.

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Configure the Gemini API key

Create a `.env` file inside the `Task2` directory and add:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Replace the placeholder with your own Gemini API key. Never share or commit the real key.

### 6. Run the application

```bash
python -m streamlit run app.py --server.fileWatcherType none
```

Streamlit will provide a local URL, usually `http://localhost:8501`.

## Testing

The application can be tested using the following scenarios:

- Upload a PDF and ask questions about its contents.
- Upload a TXT file and verify the generated answers.
- Ask questions whose answers are present in the document.
- Ask questions about information absent from the document.
- Test empty or unreadable documents.
- Verify that the application handles API errors appropriately.

## Learning Outcomes

Through this project, I learned the fundamentals of Retrieval-Augmented Generation (RAG), document text extraction, text chunking, semantic embeddings, vector similarity search using FAISS, and integrating a large language model into a Streamlit application.

## Future Improvements

- Support multiple document uploads.
- Display retrieved source text with generated answers.
- Improve retrieval accuracy and document processing.
- Add document-specific chat history and deployment support.

## Author

**Debasmita Pal**

B.Tech in Computer Science and Engineering  
Institute of Engineering & Management (IEM), University of Engineering & Management, Kolkata
