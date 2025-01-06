from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def coming_soon(request):
    return render(request, 'coming_soon.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def legal_statement(request):
    return render(request, 'legal_statement.html')

""" def resources(request):
    all_resources = Place.objects.all()
    context = {
        'resources': all_resources
    }
    return render(request, 'resources.html', context) """