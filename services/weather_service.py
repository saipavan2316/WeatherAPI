import requests

from config import API_KEY, CACHE_EXPIRY
from cache.redis_client import get_cache, set_cache


def fetch_weather(city):

    cached = get_cache(city)

    if cached:
        print("Cache Hit")
        return cached

    print("Cache Miss")

    url = (
        f"https://weather.visualcrossing.com/"
        f"VisualCrossingWebServices/rest/services/"
        f"timeline/{city}"
        f"?unitGroup=metric&key={API_KEY}"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return {
            "error": response.text,
            "status_code": response.status_code
        }

    data = response.json()

    result = {
        "city": city,
        "temperature": data["currentConditions"]["temp"],
        "humidity": data["currentConditions"]["humidity"],
        "conditions": data["currentConditions"]["conditions"]
    }

    set_cache(city, result, CACHE_EXPIRY)

    return result