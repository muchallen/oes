from django.shortcuts import render,redirect


def home(request):
    return redirect('account/login')
    
def welcome(request):
    return render(request ,'oes/home.html')
