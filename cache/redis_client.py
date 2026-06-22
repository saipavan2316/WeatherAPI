import time

cache = {}


def get_cache(city):
    city = city.lower()

    if city in cache:
        data = cache[city]

        if time.time() < data["expiry"]:
            return data["value"]

        del cache[city]

    return None


def set_cache(city, value, expiry):
    cache[city.lower()] = {
        "value": value,
        "expiry": time.time() + expiry
    }