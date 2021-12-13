from django.db import models

# Create your models here.


class UserRegistration(models.Model):
    email = models.CharField(max_length=30, unique=True, blank=False)
    username = models.CharField(max_length=20, blank=False)
    password = models.CharField(max_length=50, blank=False)


class UserLogin(models.Model):
    username = models.CharField(max_length=20, blank=False)
    password = models.CharField(max_length=50, blank=False)
