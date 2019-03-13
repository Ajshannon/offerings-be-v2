from django.db import models
# from offerings_be.users.models import User
from offerings_be.profile.models import Profile


class Offerings(models.Model):
    title = models.CharField(max_length=35)
    description = models.TextField()
    address = models.CharField(max_length=100)
    image = models.URLField(max_length=200)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None)
    date = models.DateTimeField(auto_now=True)
