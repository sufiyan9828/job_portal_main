from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    contact = models.CharField(max_length=13)
    
    user_type = models.CharField(max_length=1,choices = (
        ('E',"Employeer"),
        ('J',"Job-Seeker"),
    ))
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