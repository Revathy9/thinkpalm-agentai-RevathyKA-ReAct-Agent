import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key or api_key == "YOUR_GEMINI_API_KEY":
    # Fallback to key or raise message if needed
    api_key = "YOUR_GEMINI_API_KEY"

genai.configure(
    api_key=api_key
)

model = genai.GenerativeModel(
    "gemini-1.5-flash"
)

