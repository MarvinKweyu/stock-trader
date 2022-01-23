from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.


class CustomUser(AbstractUser):
    """Custom user models"""
    email = models.EmailField(max_length=40, unique=True)
    username = models.CharField(max_length=20, unique=True)

    CHOICES = (
        ('W', 'Warehouse attendant'),
        ('R', 'Retailer'),
    )
    role = models.CharField(max_length=1, choices=CHOICES)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.email
