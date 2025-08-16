from django.db import models

# Create your models here.
class Posts(models.Model):
    job_title = models.CharField(max_length=25)
    company_name = models.CharField(max_length=30)

    job_type = models.CharField(max_length=1, choices=(
        ('F','Full Time'),
        ('P','Part Time'),
        ('O','Other'),
    ))

    job_pay = models.CharField(max_length=1, choices=(
        ('S','Salary'),
        ('H','Hourly'),
        ('O','Other'),
    ))

    company_logo = models.ImageField(null = True,blank = True)

    location = models.CharField(max_length=50)

    email_to = models.EmailField()

    url_to = models.URLField()