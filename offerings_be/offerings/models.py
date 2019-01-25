from django.db import models
from offerings_be.users.models import User


class Offerings(models.Model):
    title = models.CharField(max_length=35)
    description = models.TextField()
    phone = models.IntegerField()
    distance = models.IntegerField(default=None)
    notify = models.BooleanField(default=False)
    image = models.URLField(max_length=200)
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='name')
