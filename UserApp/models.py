from django.db import models
from datetime import datetime

# Create your models here.
class UsersInfoModel(models.Model):
    username = models.CharField(max_length=32 , unique=True)
    last_name = models.CharField(max_length=32)
    first_name = models.CharField(max_length=32)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'password']

    def __str__(self):
        return self.username


