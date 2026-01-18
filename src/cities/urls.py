from django.urls import path
from .views import CityListView, CityWeatherView

urlpatterns = [
    path("", CityListView.as_view()),
    path("<int:city_id>/weather/", CityWeatherView.as_view()),
]
