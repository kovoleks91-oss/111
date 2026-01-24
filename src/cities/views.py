import requests
from django.http import JsonResponse
from django.conf import settings
from cities.models import City


def city_weather(request, city_id):
    try:
        city = City.objects.get(id=city_id)
    except City.DoesNotExist:
        return JsonResponse({"error": "City not found"}, status=404)

    if not settings.WEATHERBIT_API_KEY:
        return JsonResponse({"error": "WEATHERBIT_API_KEY not set"}, status=500)

    url = "https://api.weatherbit.io/v2.0/current"
    params = {
        "city": city.name,
        "country": city.country,
        "key": settings.WEATHERBIT_API_KEY,
        "units": "M",
    }

    response = requests.get(url, params=params, timeout=10)

    if response.status_code != 200:
        return JsonResponse(
            {
                "error": "Weatherbit API error",
                "status_code": response.status_code,
                "response": response.text,
            },
            status=502,
        )

    payload = response.json()
    data = payload["data"][0]

    return JsonResponse(
        {
            "city": city.name,
            "country": city.country,
            "temperature": data["temp"],
            "feels_like": data["app_temp"],
            "description": data["weather"]["description"],
            "wind_speed": data["wind_spd"],
            "clouds": data["clouds"],
        }
    )
