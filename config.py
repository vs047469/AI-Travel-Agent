import os
from dotenv import load_dotenv

# -----------------------------------------
# Load local .env file
# -----------------------------------------

load_dotenv()


# -----------------------------------------
# Read API key
# -----------------------------------------

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

MODEL_NAME = "openai/gpt-oss-120b"

# 🔍 Debug (temporary)
print("GROQ KEY Loaded:", GROQ_API_KEY is not None)

# 🚨 Safety check
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found. Check your .env file.")
