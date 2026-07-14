from langchain_groq import ChatGroq
from config import GROQ_API_KEY, MODEL_NAME

llm = ChatGroq(model=MODEL_NAME, api_key=GROQ_API_KEY)

def restaurant_agent(state):

    city = state["city"]

    prompt = f"""
List 5 famous restaurants in {city}.
"""

    response = llm.invoke(prompt)

    return {"restaurants": response.content}