from rest_framework import generics, permissions
from .models import SecureData
from .serializers import SecureDataSerializer

class SecureDataListCreate(generics.ListCreateAPIView):
    queryset = SecureData.objects.all()
    serializer_class = SecureDataSerializer
    permission_classes = [permissions.IsAuthenticated]
