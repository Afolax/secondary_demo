from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    _id = models.CharField(max_length=20, unique=True, null=True, blank=True)
    fullname = models.CharField(max_length=20, null=True, blank=True)
    is_student = models.BooleanField(default='False')
    is_parent = models.BooleanField(default='False')
    is_staff = models.BooleanField(default='False')
    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.email
