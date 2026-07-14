from tools.places_tool import find_places

def places_agent(state):

    city = state.get("city")

    if not city:
        return {"places": []}

    places = find_places(city)

    return {
        "places": places
    }