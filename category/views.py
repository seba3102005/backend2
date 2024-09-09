from django.shortcuts import render

# Create your views here.

def children (request):
    return render(request,'category/children.html')

def fiction (request):
    return render(request, 'category/fiction.html')

def nonfiction (request):
    return render(request, 'category/nonfiction.html')

def romance (request):
    return render(request, 'category/romance.html')

def science (request):
    return render(request, 'category/science.html')

def mystery (request):
    return render(request , 'category/mystery.html')



