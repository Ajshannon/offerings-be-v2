from rest_framework import serializers
from .models import Offerings

class OfferingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Offerings
        fields = ('id', 'title', 'description', 'address', 'image', 'profile', 'date')
        read_only_fields = ('id', 'date', )