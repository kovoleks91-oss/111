import os
import requests
from django.http import JsonResponse

def health_json(request):
    city = request.GET.get("city", "Cherkasy")

    api_key = os.getenv("WEATHERBIT_API_KEY")
    if not api_key:
        return JsonResponse({
            "ok": True,
            "source": "azure",
            "note": "WEATHERBIT_API_KEY is not set",
            "example": f"/?city={city}"
        })

    # Weatherbit current weather
    url = "https://api.weatherbit.io/v2.0/current"
    params = {"city": city, "key": api_key, "lang": "en"}
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()

    data = r.json()
    return JsonResponse({
        "ok": True,
        "source": "weatherbit",
        "city": city,
        "weatherbit": data,
    })
