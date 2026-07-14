import requests
from functools import lru_cache

@lru_cache(maxsize=50)
def find_places(city):

    # Step 1: Get city coordinates
    geo_url = "https://nominatim.openstreetmap.org/search"
    geo_params = {
        "q": city,
        "format": "json",
        "limit": 1
    }

    try:
        geo_res = requests.get(
            geo_url,
            params=geo_params,
            headers={"User-Agent": "ai-travel-agent"}
        )
        geo_res.raise_for_status()
        geo_data = geo_res.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching geolocation for {city}: {e}")
        return []

    if not geo_data:
        return []

    lat = geo_data[0]["lat"]
    lon = geo_data[0]["lon"]

    # Step 2: Overpass query for tourist places
    overpass_url = "https://overpass-api.de/api/interpreter"

    query = f"""
    [out:json];
    node
      (around:5000,{lat},{lon})
      ["tourism"];
    out;
    """

    try:
        response = requests.post(overpass_url, data=query)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching places from Overpass API: {e}")
        return []

    places = []

    for element in data.get("elements", []):
        name = element.get("tags", {}).get("name")

        if name and name not in places:
            places.append(name)

        if len(places) >= 6:
            break

    return places