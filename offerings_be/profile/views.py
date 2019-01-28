from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from .models import Profile
from offerings_be.users.permissions import IsUserOrReadOnly
from .serializers import ProfileSerializer


class ProfileViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Updates and retrieves user accounts
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsUserOrReadOnly,)


class ProfileCreateViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """
    Creates user accounts
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (AllowAny,)
