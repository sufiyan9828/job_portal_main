from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    dob = models.DateField(null=True, blank=True)  # Your custom field

    def __str__(self):
        return self.username