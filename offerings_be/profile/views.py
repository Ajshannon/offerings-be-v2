from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from .models import Profile
from offerings_be.users.permissions import IsUserOrReadOnly
from .serializers import ProfileSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView

class ProfileViewSet(viewsets.ModelViewSet, RetrieveUpdateDestroyAPIView):
    """
    Updates and retrieves user accounts
    """
    lookup_field = 'user'
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (AllowAny,)


