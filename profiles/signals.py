from .models import Profile
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=User)
def post_save_create_profile(sender, instance, created, *args, **kwargs):
    """
    Creation d'un profile automatiquement
    """
    if created:
        Profile.objects.create(user=instance)
