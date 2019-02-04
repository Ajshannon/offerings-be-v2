from rest_framework import serializers
from .models import Offerings

class OfferingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Offerings
        fields = ('id', 'profile', 'title', 'description', 'phone', 'distance', 'notify', 'image', 'date')
        read_only_fields = ('id', 'date', )