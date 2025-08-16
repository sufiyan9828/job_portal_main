from django.forms import ModelForm
# from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Posts

class PostForm(ModelForm):
    class Meta:
        model = Posts
        fields =  ['job_title','company_name','job_type','job_pay_type','company_logo','location','email_to','description']