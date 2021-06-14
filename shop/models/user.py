from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=500)
    active = models.BooleanField(default=True)
    phone = models.CharField(null=True, max_length=12)