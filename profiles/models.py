from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Profile model."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """String representation of the model."""
        return self.user.username
