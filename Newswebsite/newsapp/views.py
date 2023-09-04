from django.shortcuts import render, redirect
from .models import News, Topic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    news = News.objects.filter(
        Q(topic__name__icontains=q)
    )
    topics = Topic.objects.all()
    context = {'news':news, 'topics': topics}
    return render(request, 'newsapp/home.html', context)

def addnews(request):
    return render(request, 'newsapp/addnews.html')

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'USER NOT FOUND')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'USERNAME OR PASSWORD IS NOT MACHED')
    context = {'page':page}
    return render(request,'newsapp/login_register.html', context)

def logoutpage(request):
    logout(request)
    return redirect('home')