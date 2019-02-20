from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from .models import User
from .permissions import IsUserOrReadOnly
from .serializers import UserSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView

class UserViewSet(viewsets.ModelViewSet, RetrieveUpdateDestroyAPIView):
    """
    Updates and retrieves user accounts
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
