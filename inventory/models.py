from django.db import models

# Create your models here.
class Posts(models.Model):
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)

    job_type = models.CharField(max_length=1, choices=(
        ('F','Full Time'),
        ('P','Part Time'),
        ('O','Other'),
    ))

    job_pay_type = models.CharField(max_length=1, choices=(
        ('S','Salary'),
        ('H','Hourly'),
        ('O','Other'),
    ))

    company_logo = models.ImageField(null = True,blank = True)


    email_to = models.EmailField()  

    # url_to = models.URLField()

    description = models.TextField(null=True,blank=True)