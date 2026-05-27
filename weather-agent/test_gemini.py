import os
import sys
from dotenv import load_dotenv

# Try to resolve relative backend path
backend_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "backend")
dotenv_path = os.path.join(backend_dir, ".env")
load_dotenv(dotenv_path)

api_key = os.getenv("GEMINI_API_KEY")
print("Resolved .env path:", dotenv_path)
print("Does .env exist?", os.path.exists(dotenv_path))
print("API Key loaded:", api_key)

if api_key:
    # Partially mask the key for safety
    masked_key = api_key[:6] + "..." + api_key[-4:] if len(api_key) > 10 else api_key
    print(f"Masked API Key: {masked_key}")
else:
    print("No API Key loaded!")

try:
    import google.generativeai as genai
    print("Google GenerativeAI library imported successfully.")
    genai.configure(api_key=api_key)
    print("Calling GenerativeModel('gemini-2.5-flash')...")
    model = genai.GenerativeModel("gemini-2.5-flash")
    print("Generating simple test response...")
    response = model.generate_content("Hi! Respond with just the word 'Success'.")
    print("Response text:", response.text)
except Exception as e:
    print("Error encountered during API call:", type(e), e)
