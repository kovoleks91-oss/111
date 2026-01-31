from django.contrib import admin
from django.urls import path
from .views import health_json

urlpatterns = [
    path("", health_json),
    path("admin/", admin.site.urls),
]
