from django.shortcuts import render,redirect
from account import views

def home(request):
    return redirect('account/login')
    
def welcome(request):

    return render(request ,'oes/home.html',{'user':views.user})
