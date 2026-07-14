import json
import re
from functools import lru_cache
from langchain_groq import ChatGroq
from config import GROQ_API_KEY, MODEL_NAME

llm = ChatGroq(model=MODEL_NAME, api_key=GROQ_API_KEY)


@lru_cache(maxsize=100)
def get_city_cost(city, style):

    prompt = f"""
Estimate the average daily travel cost for a tourist visiting {city}.

Travel style: {style}

Return ONLY JSON:

{{
  "hotel_per_day": number,
  "food_per_day": number,
  "transport_per_day": number,
  "activities_per_day": number
}}
"""

    response = llm.invoke(prompt)

    content = response.content

    json_match = re.search(r"\{.*\}", content, re.DOTALL)

    if json_match:
        return json.loads(json_match.group())

    # fallback values
    return {
        "hotel_per_day": 100,
        "food_per_day": 40,
        "transport_per_day": 20,
        "activities_per_day": 30
    }


def cost_agent(state):

    city = state["city"]
    days = state["days"]
    style = state.get("travel_style", "mid-range")

    cost_data = get_city_cost(city, style)

    hotel = cost_data["hotel_per_day"] * days
    food = cost_data["food_per_day"] * days
    transport = cost_data["transport_per_day"] * days
    activities = cost_data["activities_per_day"] * days

    total = hotel + food + transport + activities

    return {
        "cost": {
            "hotel": hotel,
            "food": food,
            "transport": transport,
            "activities": activities,
            "total": total
        }
    }