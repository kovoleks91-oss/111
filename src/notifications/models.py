from django.db import models
from django.conf import settings
from django.db import models
from cities.models import City

User = settings.AUTH_USER_MODEL

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    temperature = models.FloatField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user} ({self.city})"
