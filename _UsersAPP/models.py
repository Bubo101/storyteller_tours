from django.db import models
from django.contrib.auth.models import User

class Storyteller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bio = models.TextField()
    credentials = models.CharField(max_length=255)

class Historian(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bio = models.TextField()
    credentials = models.CharField(max_length=255)
    verified = models.BooleanField()

