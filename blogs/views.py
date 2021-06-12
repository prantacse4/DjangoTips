from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from .models import *
from django.db.models import Q
from django.shortcuts import redirect
from  django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Count
from .forms import  PostForm


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('id')
    diction = {'posts':posts}
    return render(request, 'blogs/index.html', context = diction)


@login_required(login_url='loginpage')
def create(request):
    myform = PostForm()
    if request.method == "POST":
        myform = PostForm(request.POST, request.FILES)
        if myform.is_valid():
            myform.save(commit=True)
            messages.info(request, 'Posted')
            return redirect('index')
    diction = {'myform':myform}
    return render(request, 'blogs/create.html', context = diction)

def wrong(request):
    diction = {}
    return render(request, 'accounts/wrong.html', context = diction)

@login_required(login_url='loginpage')
def deletepost(request, id):
    if request.method == 'POST':
        delete_data = Post.objects.get(pk=id)
        if(delete_data.user == request.user):
            delete_data.delete()
            messages.info(request, 'Deleted')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def search(request):
    givenSearch = request.GET['search']
    results = Post.objects.filter( Q(topic__icontains = givenSearch ) | Q(blog__icontains = givenSearch ) )
    searchCount = results.count()
    diction = {  'givenSearch':givenSearch, 'results':results, 'searchCount':searchCount}
    return render(request, 'blogs/search.html', context = diction)
