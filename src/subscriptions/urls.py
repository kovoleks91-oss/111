from django.urls import path
from .views import SubscriptionListCreateView, SubscriptionDeleteView

urlpatterns = [
    path('', SubscriptionListCreateView.as_view(), name='subscription-list-create'),
    path('<int:pk>/', SubscriptionDeleteView.as_view(), name='subscription-delete'),
]
