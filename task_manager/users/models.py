from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    timestamp = models.DateTimeField(auto_now_add=True)
