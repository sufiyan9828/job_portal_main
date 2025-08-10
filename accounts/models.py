from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    dob = models.DateField(null=True, blank=True)  # Your custom field

    def __str__(self):
        return self.username

class Address(models.Model):
    title = models.CharField(max_length=40)
    address_line_one = models.CharField(max_length=50)
    address_line_two = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)