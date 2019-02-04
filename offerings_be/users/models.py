import uuid
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.utils.encoding import python_2_unicode_compatible
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from offerings_be.profile.models import Profile


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # change the save model for the user class and make it create a profile 
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        # checks to see whether or not the user already has a profile.
        if hasattr(self, 'profile'):
            print("has profile")

        else:
            user_profile = Profile(user=self)
            user_profile.save()

    

    def __str__(self):
        return self.username
 

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
