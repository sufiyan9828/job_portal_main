from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.views import View
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate,logout
# Create your views here.

class Register(View):
    def get(self,request):
        form = RegisterForm()
        context = {
            'form':form
        }
        return render(request,'accounts/register.html',context)
    
    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user.user_type == 'E':
                profile = EmployerProfile.objects.create(user=user)
            elif user.user_type == 'J':
                profile = JobSeekerProfile.objects.create(user = user)
            messages.success(request,f"Account Created successfully, Now Login {user.username}")
            return redirect('login')
        else:
            context = {
            'form': form
        }
        messages.error(request,"Form is Not Valid")
        return render(request,'accounts/register.html',context)
    
class Login(View):
    def get(self,request):
        form = LoginForm()
        context = {
            'form': form
        }
        return render(request,'accounts/login.html',context)
    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,username = username, password = password)
            if user:
                login(request,user)
                messages.success(request,"Login Successfull")
                return redirect('home')
            else:
                context = {
                'form':form
                }
                messages.error(request,"Invalid Credentials")
                return render(request,'accounts/login.html',context)
        else:
            context = {
                'form':form
                }
            messages.error(request,"Form is Not Valid")
            return render(request,'accounts/login.html',context)
        
class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('/')
    
    def post(self,request):
        logout(request)
        return redirect('/')

def profile_details(request):
        user = request.user 
        if request.user.user_type == 'E':
            profile = get_object_or_404(EmployerProfile,user=user)
            context = {
                'profile': profile
            }
            return render(request,'accounts/profile.html',context)
        elif request.user.user_type == 'J':
            profile = get_object_or_404(JobSeekerProfile,user=user)
            context = {
                'profile': profile
            }
            return render(request,'accounts/profile.html',context)
        else:
            profile = None
            context = {
            'profile': profile
            }
            return render(request,'accounts/profile.html',context)
        
@login_required
def profile_update(request):
    user = request.user
    if user.user_type == 'J':
        profile = get_object_or_404(JobSeekerProfile, user=user)
        if request.method == "POST":
          form = JobSeekerProfileForm(request.POST,instance=profile)
          if form.is_valid():
               form.save()
               return redirect('profile_details')
          else:
               context={
                    'form':form
               }
               return render(request,'accounts/profile_update.html',context)
        elif request.method == "GET":
          form = JobSeekerProfileForm(instance=profile)
          context={
               'form':form
          }
          return render(request,'accounts/profile_update.html',context)
        
    elif user.user_type == 'E':
        profile = get_object_or_404(EmployerProfile, user=user)
        if request.method == "POST":
          form = EmployerProfileForm(request.POST,instance=profile)
          if form.is_valid():
               form.save()
               return redirect('profile_details')
          else:
               context={
                    'form':form
               }
               return render(request,'accounts/profile_update.html',context)
        elif request.method == "GET":
          form = EmployerProfileForm(instance=profile)
          context={
               'form':form
          }
          return render(request,'accounts/profile_update.html',context)