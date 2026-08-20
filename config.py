import os
from dotenv import load_dotenv

# ✅ Load .env file
load_dotenv()

# ✅ Read environment variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

MODEL_NAME = "openai/gpt-oss-120b"

# 🔍 Debug (temporary)
print("GROQ KEY Loaded:", GROQ_API_KEY is not None)

# 🚨 Safety check
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found. Check your .env file.")
