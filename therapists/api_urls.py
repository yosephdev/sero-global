from django.urls import path
from .views import (
    TherapistProfileListCreateAPIView,
    TherapistProfileRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('', TherapistProfileListCreateAPIView.as_view(), name='therapist-list-create'),
    path('profile/', TherapistProfileRetrieveUpdateDestroyAPIView.as_view(), name='therapist-profile'),
]