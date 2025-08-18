from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    contact = models.CharField(max_length=13)
    
    user_type = models.CharField(max_length=1,choices = (
        ('E',"Employer"),
        ('J',"Job-Seeker"),
    ))

    gender = models.CharField(max_length=3, default="Not Specified" ,choices=(
          ('M',"Male"),
          ('F',"Female"),
          ('o',"other"),
          ('N/A',"Don't Want to mention")
     ))

    def __str__(self):
        return self.username    
    
class JobSeekerProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    educations = models.CharField(max_length=200,blank=True)
    skills = models.CharField(max_length=200,blank=True)
    experience = models.CharField(max_length=200, blank=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)

class EmployerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)