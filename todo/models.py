# from user_profile.models import Profile

from django.db import models
from django.urls import reverse

from profiles.models import Profile


# Create your models here.
class Task(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120)
    description = models.TextField()
    task_done = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_on',)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        # print([self.slug])
        return reverse("todo:task_detail", args=[self.slug])
