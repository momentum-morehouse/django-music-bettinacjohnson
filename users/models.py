from django.db import models
from django.contrib.auth.models import AbstractUser
# import datetime


# Consider creating a custom user model from scratch as detailed at
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#specifying-a-custom-user-model


class User(AbstractUser):
    # name = models.CharField(max_length=255)
    # email = models.EmailField(null=True, blank=True)
    # password = models.CharField(max_length=100)

    # def __str__(self):
    #   return f"{self.name}"
    pass 
