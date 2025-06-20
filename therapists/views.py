from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from rest_framework import generics, permissions
from .models import TherapistProfile
from .forms import TherapistProfileForm
from .serializers import TherapistProfileSerializer


# Frontend Views
class TherapistListView(ListView):
    model = TherapistProfile
    template_name = 'therapists/list.html'
    context_object_name = 'therapists'
    paginate_by = 12
    
    def get_queryset(self):
        return TherapistProfile.objects.filter(is_available=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Find a Therapist'
        return context


class TherapistDetailView(DetailView):
    model = TherapistProfile
    template_name = 'therapists/detail.html'
    context_object_name = 'therapist'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Dr. {self.object.user.get_full_name()}'
        return context


class TherapistProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'therapists/profile.html'
    login_url = reverse_lazy('core:login')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'My Profile'
        
        # Get or create therapist profile
        profile, created = TherapistProfile.objects.get_or_create(
            user=self.request.user
        )
        context['profile'] = profile
        return context


class TherapistProfileEditView(LoginRequiredMixin, UpdateView):
    model = TherapistProfile
    form_class = TherapistProfileForm
    template_name = 'therapists/profile_edit.html'
    success_url = reverse_lazy('therapists:profile')
    login_url = reverse_lazy('core:login')
    
    def get_object(self):
        profile, created = TherapistProfile.objects.get_or_create(
            user=self.request.user
        )
        return profile
    
    def form_valid(self, form):
        messages.success(self.request, 'Your profile has been updated successfully!')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Profile'
        return context


# API Views
class TherapistProfileListCreateAPIView(generics.ListCreateAPIView):
    queryset = TherapistProfile.objects.all()
    serializer_class = TherapistProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TherapistProfileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TherapistProfile.objects.all()
    serializer_class = TherapistProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return get_object_or_404(TherapistProfile, user=self.request.user)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)