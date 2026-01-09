from unittest.mock import patch
from django.test import TestCase
from rest_framework.test import APIClient

from cities.models import City
from src.services.weather import get_current_weather


class WeatherServiceTest(TestCase):

    @patch("src.services.weather.requests.get")
    def test_get_current_weather_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "data": [
                {
                    "temp": 5.5,
                    "weather": {
                        "description": "Cloudy"
                    }
                }
            ]
        }

        result = get_current_weather(49.4444, 32.0598)

        self.assertEqual(result["temperature"], 5.5)
        self.assertEqual(result["description"], "Cloudy")

    @patch("src.services.weather.requests.get")
    def test_get_current_weather_api_error(self, mock_get):
        mock_get.return_value.status_code = 500
        mock_get.return_value.raise_for_status.side_effect = Exception("API error")

        result = get_current_weather(49.4444, 32.0598)

        self.assertIsNone(result["temperature"])
        self.assertEqual(
            result["description"],
            "weather service temporarily unavailable"
        )


class CityWeatherEndpointTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.city = City.objects.create(
            name="Cherkasy",
            country="UA",
            latitude=49.4444,
            longitude=32.0598,
        )

    @patch("cities.views.get_current_weather")
    def test_city_weather_endpoint_success(self, mock_weather):
        mock_weather.return_value = {
            "temperature": 10.0,
            "description": "Clear sky",
        }

        response = self.client.get(
            f"/api/cities/{self.city.id}/weather/"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["city"], "Cherkasy")
        self.assertEqual(response.data["temperature"], 10.0)
        self.assertEqual(response.data["description"], "Clear sky")
