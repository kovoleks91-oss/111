from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import City
from .serializers import CitySerializer
from services.weather import get_current_weather


class CityListView(ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CityWeatherView(APIView):
    permission_classes = []

    def get(self, request, city_id):
        city = get_object_or_404(City, id=city_id)

        weather = get_current_weather(
            lat=city.latitude,
            lon=city.longitude,
        )

        return Response({
            "city": city.name,
            "temperature": weather["temperature"],
            "description": weather["description"],
        })
