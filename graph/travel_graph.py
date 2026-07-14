from langgraph.graph import StateGraph
from typing import TypedDict

from agents.intent_agent import intent_agent
from agents.weather_agent import weather_agent
from agents.places_agent import places_agent
from agents.hotel_agent import hotel_agent
from agents.restaurant_agent import restaurant_agent
from agents.flight_agent import flight_agent
from agents.cost_agent import cost_agent
from agents.itinerary_agent import itinerary_agent
from agents.city_image_agent import city_image_agent


class TravelState(TypedDict):

    query: str
    city: str
    days: int
    travel_style: str
    weather: dict
    places: list
    hotels: list
    restaurants: list
    flights: list
    cost: dict
    itinerary: str
    city_images: list

def build_graph():

    graph = StateGraph(TravelState)

    graph.add_node("intent", intent_agent)
    graph.add_node("weather", weather_agent)
    graph.add_node("places", places_agent)
    graph.add_node("hotel", hotel_agent)
    graph.add_node("restaurant", restaurant_agent)
    graph.add_node("flight", flight_agent)
    graph.add_node("itinerary", itinerary_agent)
    graph.add_node("cost", cost_agent)
    graph.add_node("city_images", city_image_agent)

    graph.set_entry_point("intent")

    graph.add_edge("intent", "weather")
    graph.add_edge("intent", "places")
    graph.add_edge("intent", "hotel")
    graph.add_edge("intent", "restaurant")
    graph.add_edge("intent", "flight")
    graph.add_edge("intent", "city_images")

    graph.add_edge("weather", "itinerary")
    graph.add_edge("places", "itinerary")
    graph.add_edge("hotel", "itinerary")
    graph.add_edge("restaurant", "itinerary")

    graph.add_edge("itinerary", "cost")

    graph.set_finish_point("cost")

    return graph.compile()