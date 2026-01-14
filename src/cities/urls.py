from django.urls import path
from django.http import JsonResponse

def cities_stub(request):
    return JsonResponse([], safe=False)

urlpatterns = [
    path("", cities_stub),
]
