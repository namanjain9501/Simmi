# Create your models here.
from pickle import TRUE
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    desc = models.TextField(blank=True)
    


