from langchain_groq import ChatGroq
from config import GROQ_API_KEY, MODEL_NAME

llm = ChatGroq(model=MODEL_NAME, api_key=GROQ_API_KEY)

def flight_agent(state):

    city = state["city"]

    prompt = f"""
Suggest 3 flight options to reach {city}.
Include airline names and approximate prices.
"""

    response = llm.invoke(prompt)

    return {"flights": response.content}