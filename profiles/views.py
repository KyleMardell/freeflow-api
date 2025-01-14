from rest_framework import generics
from freeflow_api.permissions import IsOwner
from .models import Profile
from .serializers import ProfileSerializer



class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile only if you're the owner.
    """
    permission_classes = [IsOwner]
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profile.objects.filter(owner=self.request.user)