from tools.city_image_tool import get_city_images

def city_image_agent(state):

    city = state.get("city")

    if not city:
        return {"city_images": []}

    images = get_city_images(city)

    return {"city_images": images}