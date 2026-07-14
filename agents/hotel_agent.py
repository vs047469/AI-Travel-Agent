from langchain_groq import ChatGroq
from config import GROQ_API_KEY, MODEL_NAME

llm = ChatGroq(model=MODEL_NAME, api_key=GROQ_API_KEY)

def hotel_agent(state):

    city = state["city"]

    prompt = f"""
Suggest 5 hotels in {city}.
Include budget and luxury options.
"""

    response = llm.invoke(prompt)

    return {"hotels": response.content}