# Create your models here.
from email.mime import image
from pickle import TRUE
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    desc = models.TextField(blank=True)
    image = models.FileField(blank=True)
    


