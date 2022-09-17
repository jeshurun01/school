from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to="images/profiles",
        default="images/nofile.png"
    )
    biography = models.TextField(default="No Bio")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return str(self.user.username)

    # @staticmethod
    # def get_absolute_url():
    #     return reverse("profiles:profile")
