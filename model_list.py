import google.generativeai as genai
import os
from dotenv import load_dotenv 
load_dotenv() #activate api key
api_key=os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in environment variables.")
genai.configure(api_key=api_key)
print("Available Gemini Models")
for model in genai.list_models():
    if"generateContent" in model.supported_generation_methods:
        print(f"- {model.name}")
