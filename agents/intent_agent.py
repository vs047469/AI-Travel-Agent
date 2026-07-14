import json
import re
from langchain_groq import ChatGroq
from config import GROQ_API_KEY, MODEL_NAME

llm = ChatGroq(model=MODEL_NAME, api_key=GROQ_API_KEY)

def intent_agent(state):

    query = state["query"]

    prompt = f"""
Extract travel details from this query.

Return ONLY valid JSON.

Format:
{{
  "city": "",
  "days": 0,
  "budget": 0,
  "travel_style": ""
}}

Query: {query}
"""

    response = llm.invoke(prompt)

    content = response.content

    json_match = re.search(r"\{.*\}", content, re.DOTALL)

    if json_match:
        details = json.loads(json_match.group())
    else:
        details = {}

    return {
        "city": details.get("city"),
        "days": details.get("days"),
        "budget": details.get("budget"),
        "travel_style": details.get("travel_style")
    }