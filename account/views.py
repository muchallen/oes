# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.models import User

from django.shortcuts import render, redirect

# Create your views here.
user =None


def all_users(request):
    users = User.objects.all()
    return render(request, 'account/accounts_list.html',{'users':users})

def my_account(request):
    global user
    
    return render(request, 'account/myaccount.html',{'user':user})



def signup_view(request):
    global user
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()     
            login(request,user)
            return redirect('/home')
        else:
            
            return render(request, 'account/signup.html' ,{'form':form})

    form = UserCreationForm()
    return render(request, 'account/signup.html' ,{'form':form})

def login_view(request):
    global user

    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/home')
    else:
        form = AuthenticationForm()
    return render(request,'account/login.html',{'form':form})

def forget_view(request):
    return render(request, 'account/forget.html')

def logout_view(request):
    global user
    if request.method=="POST":
        logout(request)
        user=None
        return redirect('/')
    else:
        return redirect('/home')

    


