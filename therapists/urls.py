# therapists/urls.py
from django.urls import path
from .views import TherapistProfileView

urlpatterns = [
    path('profile/', TherapistProfileView.as_view(), name='therapist-profile'),
]