import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# ---------------- PAGE CONFIGURATION ----------------
st.set_page_config(
    page_title="StudyMate AI",
    page_icon="🎓",
    layout="centered",
)

# ---------------- LOAD API KEY ----------------
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = "gemini-3.8-flash"  # Correct, active model

client = genai.Client(api_key=API_KEY) if API_KEY else None

# ---------------- SESSION STATE ----------------
if "feature" not in st.session_state:
    st.session_state.feature = "Summarize Notes"

if "generated_result" not in st.session_state:
    st.session_state.generated_result = ""

# ---------------- TITLE & HEADER ----------------
st.title("🎓 StudyMate AI")
st.write("Your personal AI study companion. Choose a tool below to get started!")

# ---------------- FEATURE SELECTION ----------------
features = [
    "Summarize Notes",
    "Generate Quiz",
    "Explain a Concept",
    "Improve My Answer"
]

selected_feature = st.selectbox(
    "Select a Study Tool",
    features,
    index=features.index(st.session_state.feature)
)
st.session_state.feature = selected_feature

# Tool descriptions
descriptions = {
    "Summarize Notes": "📝 Turn lengthy notes into short, clear study summaries.",
    "Generate Quiz": "🧩 Create practice questions to test your understanding.",
    "Explain a Concept": "💡 Understand difficult topics in simple language.",
    "Improve My Answer": "✍️ Make your answer clearer, better structured, and accurate.",
}
st.info(descriptions[selected_feature])

# ---------------- INPUT SECTION ----------------
st.subheader("Your Study Material")

placeholders = {
    "Summarize Notes": "Paste your class notes, textbook content, or study material here...",
    "Generate Quiz": "Paste a topic or study notes for your practice quiz...",
    "Explain a Concept": "Enter the concept you find difficult. For example: DBMS normalization...",
    "Improve My Answer": "Paste your answer here. StudyMate will help improve it...",
}

study_input = st.text_area(
    "Content Input",
    placeholder=placeholders[selected_feature],
    height=180,
    max_chars=15000,
    label_visibility="collapsed",
)

char_count = len(study_input)
st.caption(f"📝 {char_count:,} / 15,000 characters")

response_length = st.selectbox(
    "Response detail level",
    ["Short and simple", "Balanced", "Detailed"],
    index=1,
)

# ---------------- PROMPT CREATION ----------------
def create_prompt(feature, text, detail):
    detail_instruction = {
        "Short and simple": "Keep the response short, clear, and easy to understand.",
        "Balanced": "Give a well-organized response with useful details and examples.",
        "Detailed": "Give a detailed response with explanations, examples, and key points.",
    }

    instructions = {
        "Summarize Notes": "Create a useful study summary of the provided notes using clear headings and bullet points.",
        "Generate Quiz": "Create 5 practice questions based on the provided study material (mix of multiple-choice and short-answer) with an answer key at the end.",
        "Explain a Concept": "Explain the supplied concept to a student using simple language, definitions, and an everyday example.",
        "Improve My Answer": "Improve the student's answer while preserving its intended meaning, correcting grammar, and listing key improvements.",
    }

    return f"""
You are StudyMate AI, a friendly and responsible study assistant.

TASK:
{instructions[feature]}

RESPONSE STYLE:
{detail_instruction[detail]}

IMPORTANT RULES:
- Focus on the student's supplied content.
- Be accurate, clear, and helpful.

STUDENT'S INPUT:
{text}
"""

# ---------------- GENERATE RESPONSE ----------------
if st.button("✨ Generate with StudyMate AI", type="primary", use_container_width=True):
    if not study_input.strip():
        st.warning("Please enter some notes, a topic, or an answer first.")

    elif client is None:
        st.error("Gemini API key not found. Check that GEMINI_API_KEY is set in your .env file.")

    else:
        prompt = create_prompt(selected_feature, study_input.strip(), response_length)

        try:
            with st.spinner("StudyMate is thinking... ✨"):
                response = client.models.generate_content(
                    model=MODEL,
                    contents=prompt,
                )

            result = response.text

            if result and result.strip():
                st.session_state.generated_result = result.strip()
            else:
                st.session_state.generated_result = ""
                st.warning("The AI returned an empty response. Please try again.")

        except Exception as error:
            st.session_state.generated_result = ""
            st.error("Sorry, server traffic is high right now (503). Please wait a few seconds and try clicking generate again.")
            with st.expander("Technical details"):
                st.caption(str(error))

# ---------------- DISPLAY RESULT ----------------
if st.session_state.generated_result:
    st.divider()
    st.subheader("🌟 Your study result")

    st.markdown(st.session_state.generated_result)

    st.download_button(
        label="⬇️ Download your result",
        data=st.session_state.generated_result,
        file_name="studymate_result.txt",
        mime="text/plain",
        use_container_width=True,
    )

    if st.button("🧹 Clear result", use_container_width=True):
        st.session_state.generated_result = ""
        st.rerun()

# ---------------- HOW IT WORKS EXPANDER ----------------
with st.expander("🔎 How StudyMate AI works"):
    st.markdown(
        """
        1. **Enter your content:** Add notes, a concept, or an answer.
        2. **Choose a tool:** Select summarization, quiz generation, concept explanation, or answer improvement.
        3. **Generate:** The app builds a structured prompt and sends it to the Gemini API.
        4. **View & Download:** Read your tailored study output and download it if needed.
        """
    )