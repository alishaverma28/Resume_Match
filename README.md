# 📄 AI Resume Skill Matcher  
### *AI-Assisted Resume & Job Description Analyzer*

🚀 **Live App:**  
👉 https://resumecheckerdetails.streamlit.app/

---

## 🧠 Overview

**AI Resume Skill Matcher** is a smart web application that evaluates how well a resume matches a given job description using **Google Gemini AI**.  
It helps candidates understand their **ATS score**, identify **skill gaps**, and generate **job-optimized resumes** to improve shortlisting chances.

This tool is especially useful for:
- Job seekers preparing for ATS-based screenings  
- Freshers & professionals tailoring resumes  
- Career counselors & mentors  

---

## ✨ Key Features

- ✅ Upload resume (**PDF only**)  
- ✅ Paste job description  
- ✅ AI-generated **ATS Match Score (%)**  
- ✅ Keyword match & missing skills analysis  
- ✅ **Profile selection probability**  
- ✅ **SWOT analysis** (Strengths, Weaknesses, Opportunities, Threats)  
- ✅ Resume improvement suggestions  
- ✅ **Two AI-optimized resumes** customized for the job  
- ✅ Copy-ready format (Word → PDF friendly)  

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| **Python** | Core application logic |
| **Streamlit** | Web UI |
| **Google Gemini AI** | Resume & JD analysis |
| **dotenv** | Secure API key handling |
| **PDF Text Extraction** | Resume parsing |

---

## 🧩 Project Structure

```text
resume-skill-matcher/
│
├── app.py
├── pdf_text_extractor.py
├── requirements.txt
├── .env
└── README.md

```

---

## 🔐 Environment Setup

1.1️⃣ Clone the Repository
git clone https://github.com/your-username/resume-skill-matcher.git
cd resume-skill-matcher

2️⃣ Create Virtual Environment (Recommended)
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Add Gemini API Key

Create a .env file:

GOOGLE_API_KEY=your_google_gemini_api_key


⚠️ Never push .env to GitHub

▶️ Run the Application
streamlit run app.py

---
## 🧪 How It Works

Upload your resume (PDF)

Paste the job description

AI compares:

Skills

Keywords

Experience alignment

Gemini generates:

ATS score

SWOT analysis

Optimized resumes

---

## 📌 Use Cases

Resume ATS optimization

Skill gap analysis

Interview preparation

Career guidance tools

Placement & training institutes

---

## 🔮 Future Enhancements

📊 Skill match visualization

📁 DOCX resume upload

🧠 Multi-JD comparison

💾 Resume history & download

🌐 LinkedIn profile analysis

---

## 🤝 Contributing

Contributions are welcome!
Feel free to:

Open issues

Submit pull requests

Suggest new features

---

## 📜 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

Alisha Verma
🎓 MCA | Cloud & Data Enthusiast
☁️ AWS | Python | SQL | AI Projects

🔗 Let’s connect and build smarter career tools! 🚀





