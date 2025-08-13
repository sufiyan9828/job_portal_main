from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'main/home.html')

# Create your views here.

def faq(request):
    return render(request,'main/faq.html')

def jobs(request):
    return render(request,'main/jobs.html')

def posts(request):
    return render(request,'main/posts.html')