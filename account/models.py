from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager
# Create your models here.
class User(AbstractUser):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=30)
    photo = models.ImageField(upload_to="profile")


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [password]

    objects = CustomUserManager()
