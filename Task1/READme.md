# StudyMate AI 🎓 (Beginner Level Internship Track)

StudyMate AI is a lightweight, AI-powered student utility web application built using **Python**, **Streamlit**, and the **Google GenAI SDK**. It helps students simplify their study workflow by summarizing lecture notes, generating practice quizzes, breaking down complex concepts, and refining written answers.

---

## ✨ Features

StudyMate AI provides four core utility tools designed for everyday student learning:

1. **📝 Summarize Notes:** Converts lengthy textbook content or class notes into concise, structured summaries with key headings and bullet points.
2. **🧩 Generate Quiz:** Creates 5 targeted practice questions (a mix of multiple-choice and short answer) complete with an answer key.
3. **💡 Explain a Concept:** Breaks down difficult academic topics into simple terms, clear definitions, and practical everyday examples.
4. **✍️ Improve My Answer:** Refines grammar, tone, and logical structure for student-written answers while preserving the original meaning.

---

## 🛠️ Tech Stack

- **Frontend & UI:** [Streamlit](https://streamlit.io/)
- **AI Model & API:** Google Gemini (`gemini-3.8-flash`) via the official `google-genai` SDK
- **Environment Management:** `python-dotenv`

---

## 📂 Project Structure

```text
studymate-ai/
├── screenshots/
│   ├── summarize_notes/
│   │   ├── output_1.png
│   │   └── output_2.png
│   ├── generate_quiz/
│   │   ├── output_1.png
│   │   └── output_2.png
│   ├── explain_concept/
│   │   ├── output_1.png
│   │   └── output_2.png
│   └── improve_answer/
│       ├── output_1.png
│       └── output_2.png
├── .env                  # Local environment variables (API Key)
├── .gitignore            # Files to exclude from Git
├── requirements.txt      # Python package dependencies
├── README.md             # Project documentation
└── app.py                # Main Streamlit application