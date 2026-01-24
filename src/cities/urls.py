from django.urls import path
from .views import city_weather

urlpatterns = [
    path("weather/<int:city_id>/", city_weather),
]
