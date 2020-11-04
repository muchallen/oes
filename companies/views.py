# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .import forms, models

# Create your views here.

def company(request):
    companies = models.Company.objects.all()
    return render(request, 'companies/companies.html',{"companies":companies})

def add_company(request):
    if(request.method=="POST"):
        form = forms.AddCompany(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('/companies')
    form = forms.AddCompany()
    return render(request, 'companies/add_company.html',{'form':form})

def view_company(request):
    return render(request, 'companies/view_company.html')