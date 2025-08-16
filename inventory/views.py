from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from .forms import PostForm

# Create your views here.
def jobs(request):
    return render(request,'inventory/jobs.html')

def posts(request):
    return render(request,'inventory/posts.html')

class Post(View):
    def get(self,request):
        form = PostForm()
        return render(request,'inventory/posts.html',{'form': form})
    
    def post(self,request):
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Job is Posted')
            return redirect('jobs')
        else:
            # form = PostForm()
            messages.error(request,"""Job isn't Posted! Reason: Form is Not Valid""")
            return render(request,'inventory/posts.html',{'form': form})