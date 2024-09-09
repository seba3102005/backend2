from django.shortcuts import render
from .form import Login_form
from .models import Login
# Create your views here.
def home (request):
    return render(request, 'pages/home.html')

def rent(request):
    return render(request, 'pages/rent.html')

def index (request):
    return render(request, 'pages/index.html')

def login (request):

    if request.method=='POST':
         data_form=(Login_form(request.POST))
         if data_form.is_valid():
            data_form.save() 
             
    return render(request ,'pages/login.html',{'lf':Login_form})

def sell (request):
    return render(request, 'pages/sell.html')

def shop (request):
    return render(request, 'pages/shop.html')
