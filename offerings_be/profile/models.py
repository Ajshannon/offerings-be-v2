from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# from offerings_be.users.models import User

class Profile(models.Model):
    user = models.OneToOneField("users.User", on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=50, default="username", null=True, blank=True)
    phone_number = PhoneNumberField(blank=True, null=True, unique=True)
    profile_image = models.URLField(max_length=200, null=True, blank=True)


    def __str__(self):
        return self.username
 