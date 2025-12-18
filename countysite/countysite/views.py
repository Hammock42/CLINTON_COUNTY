from django.shortcuts import render



def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def coming_soon(request):
    return render(request, 'coming-soon.html')

def privacy_policy(request):
    return render(request, 'privacy-policy.html')

def legal_statement(request):
    return render(request, 'legal-statement.html')