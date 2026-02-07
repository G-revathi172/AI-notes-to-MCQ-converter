import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Gemini 2.5 Flash model
model = genai.GenerativeModel("gemini-2.5-flash")

# Streamlit UI
st.set_page_config(page_title="AI Notes to MCQ Generator", layout="centered")

st.title("📘 AI Notes to MCQ Generator")
st.subheader("Powered by Gemini 2.5 Flash")

notes = st.text_area(
    "Paste your study notes below 👇",
    height=250,
    placeholder="Enter notes here..."
)

num_questions = st.slider("Number of MCQs", 5, 20, 10)

difficulty = st.selectbox(
    "Difficulty Level",
    ["Easy", "Medium", "Hard"]
)

if st.button("Generate MCQs 🚀"):
    if notes.strip() == "":
        st.warning("Please enter some notes.")
    else:
        with st.spinner("Generating MCQs using Gemini AI..."):
            prompt = f"""
            Convert the following notes into {num_questions} {difficulty} level MCQs.
            Each question should have:
            - Question
            - Four options (A, B, C, D)
            - Correct answer

            Notes:
            {notes}
            """

            response = model.generate_content(prompt)
            st.success("MCQs Generated Successfully ✅")
            st.markdown(response.text)
