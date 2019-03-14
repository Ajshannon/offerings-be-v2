from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator

class Profile(models.Model):
    user = models.OneToOneField("users.User", on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=50, default="username", null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    profile_image = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.username
 