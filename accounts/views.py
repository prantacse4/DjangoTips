from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from .models import *
from django.db.models import Q
from django.shortcuts import redirect
from  django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Count
from .forms import  UserCreationForm
from blogs.models import *


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def loginpage(request):
    if(request.user.is_authenticated):
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                if request.user.is_superuser == True:
                    return HttpResponseRedirect('/admin')
                return redirect('profile')
            
            else:
                messages.info(request, 'Incorrect Username or Password')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        
    diction = {}
    return render(request, 'accounts/login.html')


def signuppage(request):
    if(request.user.is_authenticated):
        return redirect('/')
    else:
        myform = UserCreationForm()
        if request.method == 'POST':
            myform = UserCreationForm(request.POST)
            if myform.is_valid():
                myform.save(commit=True)
                user = myform.cleaned_data.get('username')
                messages.success(request, 'Account Created for '+ user)
                return redirect('loginpage')

        diction = {'myform':myform}
        return render(request, 'accounts/signup.html', context = diction)


# @login_required(login_url='loginpage')
# def profile(request):
#     user = request.user
#     user = User.objects.get(pk=user.id)
#     profile = Profile.objects.filter(user=request.user)
#     if profile:
#         profile = Profile.objects.get(pk=user)
#     diction = {'profile':profile, 'user':user }
#     return render(request, 'Shop/profile.html', context = diction)

# @login_required(login_url='loginpage')
# def updateprofile(request):
#     user = request.user
#     myprofile = Profile.objects.filter(pk=user)
#     if myprofile:
#         myprofile = Profile.objects.get(pk=user)

#     diction = {'profile':myprofile}
#     return render(request, 'Shop/updateprofile.html', context = diction)


# @login_required(login_url='loginpage')
# def updateprofiledetails(request):
#     user = request.user
#     check = Profile.objects.filter(user=user)
#     if check:
#         ins = Profile.objects.get(pk=user)
#         if request.method=="POST":
#             myform = ProfileForm(request.POST,instance=ins)
#             if myform.is_valid():
#                 myform.save(commit=True)
#                 messages.success(request, 'Profile Updated')
#                 return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
#             else:
#                 diction = {'myform':myform}
#                 return render(request, 'Shop/updateprofile.html', context = diction)



@login_required(login_url='loginpage')
def logoutuser(request):
    logout(request)
    return redirect('/')


@login_required(login_url='loginpage')
def delete_my_account(request):
    if request.method == 'POST':
        userdata = request.user.id
        del_id = User.objects.get(id=userdata)
        del_id.delete()
        logout(request)
        return redirect('/')

@login_required(login_url='loginpage')
def profile(request):
    posts = Post.objects.filter(user=request.user)
    diction = {'posts':posts}
    return render(request, 'accounts/profile.html', context = diction)



