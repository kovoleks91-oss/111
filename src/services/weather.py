import requests
from django.conf import settings

OPENWEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_current_weather(lat: float, lon: float) -> dict:
    params = {
        "lat": lat,
        "lon": lon,
        "appid": settings.WEATHER_API_KEY,
        "units": "metric",
    }

    response = requests.get(OPENWEATHER_URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    return {
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
    }
