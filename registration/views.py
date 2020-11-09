# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from . import forms, models
from django.core.mail import send_mail

from exams import models as exam_models

# Create your views here.
def registration(request):
    testee = models.Testee.objects.all()
    exams = exam_models.Exam.objects.all()
    if(request.method=="POST"):
        tests = request.POST.getlist('data[0][tests][]')
        email=request.POST.get('data[1][email]')
        user = models.Testee.objects.get(email=email)



    
       
        links=[]
        for x in tests:
            links.append(x.upper()+" : http://localhost/8000/exams/assignExam/"+x)
       # print(links)
        message= 'Hello '+user.first_name+ ' ' +user.last_name + ' please follow the link to attempt your exam.\n \n'+'\n'.join(links)+'. \n \n Good luck! \n \n Regards \n \n OES'
        try:
            send_mail('oes exams', message, 'muchallen@gmail.com', [email])
        except SMTPException as e:
            print('There was an error sending an email: ', e)       
    return render(request, 'registration/registration.html',{'testees':testee, 'exams':exams})

def add_testee(request):
    if(request.method=="POST"):
        form=forms.AddTestee(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('/registration/',)

    
    form=forms.AddTestee()
    return render(request, 'registration/add_testee.html', {'form':form})

