from django.urls import path
from .views import CityListView, CityWeatherView

urlpatterns = [
    path("", CityListView.as_view(), name="city-list"),
    path("<int:city_id>/weather/", CityWeatherView.as_view(), name="city-weather"),
]
