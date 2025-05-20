from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'username', 'is_active', 'is_staff', 'is_superuser', 'is_therapist', 'is_client')
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'is_therapist', 'is_client')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'phone_number', 'date_of_birth', 'profile_picture', 'bio')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'is_therapist', 'is_client', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('email',)

# Register the custom user model
admin.site.register(User, CustomUserAdmin)