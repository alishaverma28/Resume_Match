import os
import google.generativeai as genai
import streamlit as st
from pdf_text_extractor import extract_text
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("Google Gemini API key not found in .env file")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-flash-lite-latest")

# ================= UI =================
st.header("SKILL MATCHER :blue[AI Assisted Skill Matching Tool]")
st.divider()

st.markdown("""
- Upload your resume (**PDF only**)
- Paste the **Job Description**
- Get ATS score, SWOT analysis & optimized resumes
""")

# ================= Sidebar =================
st.sidebar.header("UPLOAD YOUR RESUME")
st.sidebar.divider()
pdf_doc = st.sidebar.file_uploader("Upload Resume (PDF)", type=["pdf"])

pdf_text = None
if pdf_doc:
    pdf_text = extract_text(pdf_doc)
else:
    st.sidebar.info("Please upload a PDF resume")

# ================= Job Description =================
job_desc = st.text_area(
    "Paste Job Description (Ctrl + Enter to submit)",
    max_chars=10000
)

# ================= Gemini Prompt =================
if job_desc and pdf_text:
    prompt = f"""
You are an expert ATS and hiring specialist.

RESUME:
{pdf_text}

JOB DESCRIPTION:
{job_desc}

Tasks:
1. Calculate ATS score (%) with matching & missing keywords (max 2 lines)
2. Estimate chances of profile selection (1 line)
3. SWOT analysis in bullet points
4. Resume strengths helping shortlisting
5. Resume improvement suggestions
6. Create TWO optimized resumes tailored for this job,
   formatted so they can be directly copied into Word and exported as PDF
"""

    with st.spinner("Analyzing resume..."):
        response = model.generate_content(prompt)

    st.success("Analysis Completed")
    st.write(response.text)

elif job_desc and not pdf_text:
    st.error("Please upload your resume PDF first.")
