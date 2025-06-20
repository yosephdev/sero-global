from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from .models import ClientProfile
from .forms import ClientProfileForm


class ClientProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'clients/profile.html'
    login_url = reverse_lazy('core:login')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'My Profile'
        
        # Get or create client profile
        profile, created = ClientProfile.objects.get_or_create(
            user=self.request.user
        )
        context['profile'] = profile
        return context


class ClientProfileEditView(LoginRequiredMixin, UpdateView):
    model = ClientProfile
    form_class = ClientProfileForm
    template_name = 'clients/profile_edit.html'
    success_url = reverse_lazy('clients:profile')
    login_url = reverse_lazy('core:login')
    
    def get_object(self):
        profile, created = ClientProfile.objects.get_or_create(
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


class BookSessionView(LoginRequiredMixin, TemplateView):
    template_name = 'clients/book_session.html'
    login_url = reverse_lazy('core:login')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Book a Session'
        # Add available therapists
        from therapists.models import TherapistProfile
        context['therapists'] = TherapistProfile.objects.filter(is_available=True)
        return context


class ClientSessionsView(LoginRequiredMixin, TemplateView):
    template_name = 'clients/sessions.html'
    login_url = reverse_lazy('core:login')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'My Sessions'
        # Add user's sessions when you create the sessions model
        return context