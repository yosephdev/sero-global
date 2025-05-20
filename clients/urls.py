from django.urls import path
from .views import ClientProfileListCreateView, ClientProfileRetrieveUpdateDestroyView

urlpatterns = [
    path('profiles/', ClientProfileListCreateView.as_view(), name='client-profile-list'),
    path('profiles/<int:pk>/', ClientProfileRetrieveUpdateDestroyView.as_view(), name='client-profile-detail'),
]