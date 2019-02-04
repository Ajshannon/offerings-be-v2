from django.db import models
# from offerings_be.users.models import User


class Profile(models.Model):
    user = models.OneToOneField("users.User", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
 