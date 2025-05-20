from django.contrib import admin
from .models import ClientProfile

# Register your models here.

@admin.register(ClientProfile)
class ClientProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'gender')
    list_filter = ('gender',)
    search_fields = ('user__email', 'user__first_name', 'user__last_name', 'phone_number')
