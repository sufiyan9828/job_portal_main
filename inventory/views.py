from django.shortcuts import render

# Create your views here.
def jobs(request):
    return render(request,'inventory/jobs.html')

def posts(request):
    return render(request,'inventory/posts.html')