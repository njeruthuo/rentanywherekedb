from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    national_id = models.CharField(max_length=200, unique=True)
    subscription_active = models.BooleanField(default=False)
    phone = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.username
