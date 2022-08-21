from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="profiles")
    biography = models.TextField(default="No Bio")

    def __str__(self):
        return f"Profile of {self.user.name}"
