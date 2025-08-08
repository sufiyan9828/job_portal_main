from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    contact = models.CharField(max_length=13)
    gender = models.CharField(max_length = 3, choices = (
        ('M',"Male"),
        ('F',"Female"), 
        ('O',"Other"),
        ('N/A',"Prefer not "),
    ))
    dob = models.DateField(blank=True,null=True)
    user_type = models.CharField(max_length=1,choices=(
        ('J',"Job Seeker"),
        ('E',"Emplyeer"),
        ('A',"Admin"),
    ))

class Address(models.Model):
    title = models.CharField(max_length=40)
    address_line_one = models.CharField(max_length=50)
    address_line_Two = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=50)
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)