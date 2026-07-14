import requests
from functools import lru_cache

UNSPLASH_ACCESS_KEY = "YOUR_KEY_HERE"

@lru_cache(maxsize=50)
def get_city_images(city):

    url = "https://api.unsplash.com/search/photos"

    params = {
        "query": city,
        "per_page": 3
    }

    headers = {
        "Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"
    }

    response = requests.get(url, headers=headers, params=params)

    data = response.json()

    images = []

    for photo in data.get("results", []):
        images.append(photo["urls"]["regular"])

    return images