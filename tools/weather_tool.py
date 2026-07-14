import requests
from functools import lru_cache

@lru_cache(maxsize=50)
def get_weather(city):

    try:
        # Get coordinates of the city
        geo_url = "https://geocoding-api.open-meteo.com/v1/search"
        geo_params = {
            "name": city,
            "count": 1
        }

        geo_response = requests.get(geo_url, params=geo_params)
        geo_data = geo_response.json()

        if "results" not in geo_data:
            return {}

        lat = geo_data["results"][0]["latitude"]
        lon = geo_data["results"][0]["longitude"]

        # Get weather
        weather_url = "https://api.open-meteo.com/v1/forecast"

        weather_params = {
            "latitude": lat,
            "longitude": lon,
            "current_weather": True
        }

        weather_response = requests.get(weather_url, params=weather_params)
        weather_data = weather_response.json()

        if "current_weather" in weather_data:
            return weather_data["current_weather"]

        return {}

    except Exception as e:
        print("Weather API error:", e)
        return {}