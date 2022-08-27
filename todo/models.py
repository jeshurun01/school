# from user_profile.models import Profile

from django.db import models

from profiles.models import Profile


# Create your models here.
class Task(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.TextField(default='...')
    task_done = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)
