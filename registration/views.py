# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from . import forms, models

# Create your views here.
def registration(request):
    testee = models.Testee.objects.all()
    return render(request, 'registration/registration.html',{'testees':testee})

def add_testee(request):
    if(request.method=="POST"):
        form=forms.AddTestee(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('/registration/',)

    
    form=forms.AddTestee()
    return render(request, 'registration/add_testee.html', {'form':form})

