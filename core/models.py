from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

# Create your models here.
class User(AbstractUser):
    """
    Custom user model for Sero Global.
    """
    class Role(models.TextChoices):
        CLIENT = 'CLIENT', _('Client')
        THERAPIST = 'THERAPIST', _('Therapist')
        ADMIN = 'ADMIN', _('Admin')

    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.CLIENT
    )
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.CharField(_('phone number'), max_length=20, blank=True)
    is_therapist = models.BooleanField(_('is therapist'), default=False)
    is_client = models.BooleanField(_('is client'), default=False)
    date_of_birth = models.DateField(_('date of birth'), null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    bio = models.TextField(_('bio'), blank=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    @property
    def is_client(self):
        return self.role == self.Role.CLIENT

    @property
    def is_therapist(self):
        return self.role == self.Role.THERAPIST

    @property
    def is_admin(self):
        return self.role == self.Role.ADMIN

    class Meta:
        ordering = ['-date_joined']
        verbose_name = _('user')
        verbose_name_plural = _('users')
    


    
  
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ['-date_joined']

    def __str__(self):
        return self.email