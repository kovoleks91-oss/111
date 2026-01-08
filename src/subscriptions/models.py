from django.db import models

from django.conf import settings
from django.db import models
from cities.models import City

User = settings.AUTH_USER_MODEL

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='subscriptions')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'city')

    def __str__(self):
        return f"{self.user} -> {self.city}"
