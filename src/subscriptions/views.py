from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Subscription
from .serializers import SubscriptionSerializer

class SubscriptionListCreateView(ListCreateAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Subscription.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SubscriptionDeleteView(DestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Subscription.objects.filter(user=self.request.user)
