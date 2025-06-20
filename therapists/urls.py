from django.urls import path
from . import views

app_name = 'therapists'

urlpatterns = [
    path('', views.TherapistProfileView.as_view(), name='list'),
    path('<int:pk>/', views.TherapistProfileView.as_view(), name='detail'),
    path('profile/', views.TherapistProfileView.as_view(), name='profile'),
    path('profile/edit/', views.TherapistProfileView.as_view(), name='profile_edit'),
]