from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(("email address"), unique=True)
    tel = models.CharField(('phone'),unique=True, max_length=15)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ['name', 'email', 'tel']

    def __str__(self):
        return self.username
