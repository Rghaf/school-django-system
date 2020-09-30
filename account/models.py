from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    age = models.BooleanField(null=True, blank=True)
    image = models.ImageField(upload_to = 'profiles', null = True, blank = True, )
