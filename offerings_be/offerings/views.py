from offerings_be.users.permissions import IsUserOrReadOnly
from .serializers import OfferingsSerializer
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .models import Offerings

# class OfferingsViewSet(viewsets.GenericViewSet, RetrieveUpdateDestroyAPIView):
class OfferingsViewSet(viewsets.ModelViewSet, RetrieveUpdateDestroyAPIView):
    """
    Updates and retrieves user accounts
    """
    queryset = Offerings.objects.all()
    serializer_class = OfferingsSerializer


# class OfferingsCreateViewSet(mixins.CreateModelMixin,
#                         viewsets.GenericViewSet):
#     """
#     Creates user accounts
#     """
#     queryset = Offerings.objects.all()
#     serializer_class = OfferingsSerializer

