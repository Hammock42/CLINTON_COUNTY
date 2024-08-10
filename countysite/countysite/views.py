from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

def coming_soon(request):
    return render(request, 'coming_soon.html')