from rest_framework import serializers
from .models import Offerings

class OfferingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Offerings
        fields = ('id', 'title', 'description', 'phone', 'distance', 'notify', 'image', 'date', 'profile')
        read_only_fields = ('id', 'date', )