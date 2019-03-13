from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('id', 'user', 'username', 'phone_number', 'profile_image')
        read_only_fields = ('id', )
