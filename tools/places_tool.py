import requests
from functools import lru_cache


OVERPASS_URLS = [
    "https://overpass-api.de/api/interpreter",
    "https://overpass.kumi.systems/api/interpreter",
    "https://overpass.private.coffee/api/interpreter",
]

HEADERS = {
    "User-Agent": "AI-Travel-Planner/1.0",
    "Accept": "application/json",
}


@lru_cache(maxsize=50)
def find_places(city):

    # ---------------------------------------------------------
    # Step 1: Get city coordinates using Nominatim
    # ---------------------------------------------------------
    geo_url = "https://nominatim.openstreetmap.org/search"

    geo_params = {
        "q": city,
        "format": "json",
        "limit": 1,
    }

    try:
        geo_res = requests.get(
            geo_url,
            params=geo_params,
            headers=HEADERS,
            timeout=15,
        )

        geo_res.raise_for_status()
        geo_data = geo_res.json()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching geolocation for {city}: {e}")
        return []

    if not geo_data:
        print(f"No location found for city: {city}")
        return []

    lat = geo_data[0]["lat"]
    lon = geo_data[0]["lon"]

    # ---------------------------------------------------------
    # Step 2: Query Overpass API for tourist places
    # ---------------------------------------------------------

    query = f"""
    [out:json][timeout:25];

    node
      (around:5000,{lat},{lon})
      ["tourism"];

    out;
    """

    places = []

    for overpass_url in OVERPASS_URLS:

        try:
            print(f"Trying Overpass server: {overpass_url}")

            response = requests.post(
                overpass_url,
                data={"data": query},
                headers=HEADERS,
                timeout=60,
            )

            response.raise_for_status()

            data = response.json()

            # Successfully received response
            for element in data.get("elements", []):

                name = element.get("tags", {}).get("name")

                if name and name not in places:
                    places.append(name)

                if len(places) >= 6:
                    break

            break

        except requests.exceptions.RequestException as e:
            print(
                f"Overpass server failed: "
                f"{overpass_url} -> {e}"
            )

    # ---------------------------------------------------------
    # Step 3: Return results
    # ---------------------------------------------------------

    if not places:
        print(f"No tourist places found for {city}")

    return places[:6]