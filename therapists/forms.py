from django import forms
from .models import TherapistProfile


class TherapistProfileForm(forms.ModelForm):
    class Meta:
        model = TherapistProfile
        fields = [
            'specialization',
            'license_number',
            'years_of_experience',
            'bio',
            'hourly_rate',
            'is_available',
        ]
        widgets = {
            'specialization': forms.Select(attrs={'class': 'form-control'}),
            'license_number': forms.TextInput(attrs={'class': 'form-control'}),
            'years_of_experience': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'hourly_rate': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0'}),
            'is_available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'specialization': 'Specialization',
            'license_number': 'License Number',
            'years_of_experience': 'Years of Experience',
            'bio': 'Professional Bio',
            'hourly_rate': 'Hourly Rate ($)',
            'is_available': 'Available for new clients',
        }
