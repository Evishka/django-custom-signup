from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField("email address",unique=True)
    first_name = models.CharField("first name", max_length=30, blank=False, unique=False)
    last_name = models.CharField("last name", max_length=30, blank=False, unique=False)
    personal_url = models.URLField("personal url", max_length=255,blank=False, unique=False)
    def __str__(self):
        return self.email