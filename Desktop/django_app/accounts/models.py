from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
import uuid

class CustomUser(AbstractUser):
    
    def __str__(self):
        return self.email
        