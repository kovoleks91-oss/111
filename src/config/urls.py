from django.contrib import admin
from django.urls import path
from src.cities.views import health_json

urlpatterns = [
    path("", health_json),
    path("admin/", admin.site.urls),
]
