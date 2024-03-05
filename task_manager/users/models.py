from django.core.validators import RegexValidator
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.TextField(max_length=150, validators=[RegexValidator(r'^[\w.@+-]+$')], blank=False)
    password1 = models.CharField(max_length=200, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
