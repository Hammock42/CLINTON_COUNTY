from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def arts(request):
    return render(request, 'arts.html')

def coming_soon(request):
    return render(request, 'coming_soon.html')

def culture(request):
    return render(request, 'culture.html')

def events(request):
    return render(request, 'events.html')

def family_fun(request):
    return render(request, 'family_fun.html')

def food_drink(request):
    return render(request, 'food_drink.html')

def history_museums(request):
    return render(request, 'history_museums.html')

def music(request):
    return render(request, 'music.html')

def outdoor_adventure(request):
    return render(request, 'outdoor_adventure.html')

def place(request):
    return render(request, 'place.html')

def place_alt(request):
    return render(request, 'place_alt.html')

def shopping_leisure(request):
    return render(request, 'shopping_leisure.html')

def tours(request):
    return render(request, 'tours.html')