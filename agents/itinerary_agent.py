from langchain_groq import ChatGroq
from config import GROQ_API_KEY, MODEL_NAME

llm = ChatGroq(model=MODEL_NAME, api_key=GROQ_API_KEY)

def itinerary_agent(state):

    city = state["city"]
    days = state["days"]
    weather = state["weather"]
    places = state["places"]
    hotels = state["hotels"]
    restaurants = state["restaurants"]

    prompt = f"""
Create a {days} day travel itinerary for {city}.

Weather:
{weather}

Places:
{places}

Hotels:
{hotels}

Restaurants:
{restaurants}

Each day must have 3 activities.
"""

    response = llm.invoke(prompt)

    return {"itinerary": response.content}