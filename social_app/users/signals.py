from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
#     sender: The model class that sends the signal (User in this case).
# instance: The actual instance of the model that's sending the signal.
# created: A boolean indicating whether a new instance was created.
# **kwargs: Additional keyword arguments.
    if created:  
        Profile.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()