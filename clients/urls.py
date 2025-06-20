from django.urls import path
from . import views

app_name = 'clients'

urlpatterns = [
    path('profile/', views.ClientProfileView.as_view(), name='profile'),
    path('profile/edit/', views.ClientProfileEditView.as_view(), name='profile_edit'),
    path('book-session/', views.BookSessionView.as_view(), name='book_session'),
    path('sessions/', views.ClientSessionsView.as_view(), name='sessions'),
]
