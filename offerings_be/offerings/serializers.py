from rest_framework import serializers
# from ..profile.serializers import ProfileSerializer
from .models import Offerings

class OfferingsSerializer(serializers.ModelSerializer):
    # profile = ProfileSerializer(read_only=True)

    class Meta:
        model = Offerings
        fields = ('id', 'title', 'description', 'address', 'image', 'profile', 'date')
        read_only_fields = ('id', )