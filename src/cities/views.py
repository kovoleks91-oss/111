import requests

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import City


def city_weather(request, city_id):
    city = get_object_or_404(City, id=city_id)

    url = "https://api.weatherbit.io/v2.0/current"
    params = {
        "city": city.name,
        "country": city.country,
        "key": settings.WEATHERBIT_API_KEY,
        "units": "M",
    }

    try:
        response = requests.get(url, params=params, timeout=5)

        # 🔹 УСПІХ — віддаємо реальні дані
        if response.status_code == 200:
            payload = response.json()
            data = payload["data"][0]

            return JsonResponse(
                {
                    "source": "weatherbit",
                    "city": city.name,
                    "country": city.country,
                    "temperature": data["temp"],
                    "feels_like": data["app_temp"],
                    "description": data["weather"]["description"],
                    "wind_speed": data["wind_spd"],
                    "clouds": data["clouds"],
                }
            )

        # 🔸 API відповів, але з помилкою → fallback
        return JsonResponse(
            {
                "source": "fallback",
                "note": "Weatherbit API unavailable or restricted",
                "city": city.name,
                "country": city.country,
                "temperature": 2.0,
                "feels_like": -1.0,
                "description": "overcast clouds",
                "wind_speed": 4.5,
                "clouds": 90,
            }
        )

    except requests.RequestException:
        # 🔸 timeout / connection error → fallback
        return JsonResponse(
            {
                "source": "fallback",
                "note": "Weather service temporarily unavailable",
                "city": city.name,
                "country": city.country,
                "temperature": 1.5,
                "feels_like": -2.0,
                "description": "cloudy",
                "wind_speed": 3.8,
                "clouds": 80,
            }
        )
