from rest_framework import serializers
from .models import Profile
# from ..users.serializers import UserSerializer

class ProfileSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ('id', 'user', 'username', 'phone_number', 'profile_image')
        read_only_fields = ('id',)
