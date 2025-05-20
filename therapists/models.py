from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


# Create your models here.

class TherapistProfile(models.Model):
    class Specialization(models.TextChoices):
        CLINICAL = 'clinical', _('Clinical Psychology')
        COUNSELING = 'counseling', _('Counseling Psychology')
        FORENSIC = 'forensic', _('Forensic Psychology')
        HEALTH = 'health', _('Health Psychology')
        NEURO = 'neuro', _('Neuropsychology')
        SCHOOL = 'school', _('School Psychology')

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='therapist_profile'
    )
    specialization = models.CharField(
        max_length=20,
        choices=Specialization.choices,
        default=Specialization.CLINICAL
    )
    license_number = models.CharField(max_length=50, unique=True)
    years_of_experience = models.PositiveIntegerField(default=0)
    bio = models.TextField(blank=True)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.get_specialization_display()}"

    class Meta:
        verbose_name = _('Therapist Profile')
        verbose_name_plural = _('Therapist Profiles')