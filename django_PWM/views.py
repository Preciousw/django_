# It's work is to render
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact_us(request):
    return render(request,'contact_us.html')
