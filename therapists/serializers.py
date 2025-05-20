from rest_framework import serializers
from .models import TherapistProfile

class TherapistProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TherapistProfile
        fields = '__all__'
        read_only_fields = ('user', 'created_at', 'updated_at')