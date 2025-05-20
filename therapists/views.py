from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import TherapistProfile
from .serializers import TherapistProfileSerializer

class TherapistProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = TherapistProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):        
        profile, created = TherapistProfile.objects.get_or_create(
            user=self.request.user
        )
        return profile

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)