from .models import Offerings
from offerings_be.users.permissions import IsUserOrReadOnly
from .serializers import OfferingSerializer
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from .models import User
from .permissions import IsUserOrReadOnly
from .serializers import CreateUserSerializer, UserSerializer

class OfferingViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Updates and retrieves user accounts
    """
    queryset = Offerings.objects.all()
    serializer_class = OfferingSerializer
    permission_classes = (IsUserOrReadOnly,)


class OfferingsCreateViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """
    Creates user accounts
    """
    queryset = Offerings.objects.all()
    serializer_class = OfferingSerializer
    permission_classes = (AllowAny,)
