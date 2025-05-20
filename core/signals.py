from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal to create a profile when a new user is created.
    """
    if created:
        if instance.is_therapist:
            # Create therapist profile
            from therapists.models import TherapistProfile
            TherapistProfile.objects.get_or_create(user=instance)
        elif instance.is_client:
            # Create client profile
            from clients.models import ClientProfile
            ClientProfile.objects.get_or_create(user=instance)