from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def coming_soon(request):
    return render(request, 'coming_soon.html')

def place(request):
    return render(request, 'place.html')

def place_alt(request):
    return render(request, 'place_alt.html')