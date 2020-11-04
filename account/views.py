# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.shortcuts import render, redirect

# Create your views here.

def signup_view(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()     
            print('done')
            return redirect('account:login')
        else:
            print('failedx')
            return render(request, 'account/signup.html' ,{'form':form})

    form = UserCreationForm()
    return render(request, 'account/signup.html' ,{'form':form})

def login_view(request):
    if request.method=='POST':
        return redirect('/home')

    
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # LOGIN USER
            return redirect('/home')
    else:
        form = AuthenticationForm()
    return render(request,'account/login.html',{'form':form})

def forget_view(request):
    return render(request, 'account/forget.html')


