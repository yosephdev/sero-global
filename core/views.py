from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, UpdateView
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from .forms import CustomUserCreationForm, ContactForm
from .models import User


class HomeView(TemplateView):
    template_name = 'core/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Home'
        return context


class AboutView(TemplateView):
    template_name = 'core/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'About Us'
        return context


class ServicesView(TemplateView):
    template_name = 'core/services.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Our Services'
        return context


class ContactView(TemplateView):
    template_name = 'core/contact.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Contact Us'
        return context
    
    def post(self, request, *args, **kwargs):
        # Handle contact form submission
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        if first_name and last_name and email and message:
            try:
                # Send email notification
                full_message = f"""
                New contact form submission:
                
                Name: {first_name} {last_name}
                Email: {email}
                Phone: {phone or 'Not provided'}
                Subject: {subject or 'General Inquiry'}
                
                Message:
                {message}
                """
                
                send_mail(
                    subject=f'Contact Form: {subject or "General Inquiry"}',
                    message=full_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL],
                    fail_silently=False,
                )
                
                messages.success(request, 'Thank you for your message! We\'ll get back to you soon.')
            except Exception as e:
                messages.error(request, 'Sorry, there was an error sending your message. Please try again.')
        else:
            messages.error(request, 'Please fill in all required fields.')
        
        return redirect('core:contact')


class CustomLoginView(LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('core:dashboard')
    
    def form_valid(self, form):
        messages.success(self.request, f'Welcome back, {form.get_user().first_name or form.get_user().username}!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password. Please try again.')
        return super().form_invalid(form)


class CustomLogoutView(LogoutView):
    next_page = 'core:home'
    
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, 'You have been successfully logged out.')
        return super().dispatch(request, *args, **kwargs)


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('core:login')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        
        # Create profile based on user role
        if user.role == User.Role.CLIENT:
            from clients.models import ClientProfile
            ClientProfile.objects.create(user=user)
        elif user.role == User.Role.THERAPIST:
            from therapists.models import TherapistProfile
            TherapistProfile.objects.create(user=user)
        
        messages.success(
            self.request, 
            f'Welcome to Sero Global, {user.first_name}! Please sign in to continue.'
        )
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, 'Please correct the errors below.')
        return super().form_invalid(form)


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'core/dashboard.html'
    login_url = reverse_lazy('core:login')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        
        context['page_title'] = 'Dashboard'
        context['user_role'] = user.role
        
        # Check user role using the property correctly
        if user.role == User.Role.CLIENT:
            context['profile'] = getattr(user, 'client_profile', None)
            # Add client-specific context
            context['upcoming_appointments'] = []  # TODO: Implement appointments
            context['recent_sessions'] = []  # TODO: Implement sessions
            
        elif user.role == User.Role.THERAPIST:
            context['profile'] = getattr(user, 'therapist_profile', None)
            # Add therapist-specific context
            context['today_appointments'] = []  # TODO: Implement appointments
            context['pending_requests'] = []  # TODO: Implement booking requests
            
        return context


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'core/profile.html'
    login_url = reverse_lazy('core:login')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        
        context['page_title'] = 'My Profile'
        context['user_role'] = user.role
        
        if user.role == User.Role.CLIENT:
            context['profile'] = getattr(user, 'client_profile', None)
        elif user.role == User.Role.THERAPIST:
            context['profile'] = getattr(user, 'therapist_profile', None)
            
        return context
