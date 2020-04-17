# Create default user profile after user is created

# creating signal when user is created
from django.db.models.signals import post_save
from django.contrib.auth.models import User
# creating reciever
from django.dispatch import receiver
from .models import Profile

#receiver takes signal (post_save), sender (User)
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    #if user is created with instance of user that was created
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
# kwargs - exclude any additional key arguments
def save_profile(sender, instance, **kwargs):
    #save profile
    instance.profile.save()

