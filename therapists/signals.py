from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import TherapistProfile

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_therapist_profile(sender, instance, created, **kwargs):
    if created and instance.is_therapist:
        TherapistProfile.objects.get_or_create(user=instance)