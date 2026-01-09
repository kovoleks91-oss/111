import requests
from django.conf import settings

WEATHERBIT_URL = "https://api.weatherbit.io/v2.0/current"


def get_current_weather(lat: float, lon: float) -> dict:
    if not settings.WEATHER_API_KEY:
        return {
            "temperature": None,
            "description": "weather api key missing",
        }

    params = {
        "lat": lat,
        "lon": lon,
        "key": settings.WEATHER_API_KEY,
        "units": "M",
    }

    try:
        response = requests.get(WEATHERBIT_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        weather = data["data"][0]

        return {
            "temperature": weather["temp"],
            "description": weather["weather"]["description"],
        }

    except Exception:
        return {
            "temperature": None,
            "description": "weather service temporarily unavailable",
        }
