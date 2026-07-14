from tools.weather_tool import get_weather

def weather_agent(state):

    city = state.get("city")

    if not city:
        return {"weather": {}}

    weather = get_weather(city)

    return {
        "weather": weather
    }