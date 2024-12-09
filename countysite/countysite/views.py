from django.shortcuts import render
from places.models import Place

def index(request):
    return render(request, 'index.html')

def abbey(request):
    return render(request, 'abbey.html')

def about(request):
    return render(request, 'about.html')

def antique_show(request):
    return render(request, 'antique_show.html')

def arts(request):
    return render(request, 'arts.html')

def cameron_depot_museum(request):
    return render(request, 'cameron_depot.html')

def car_show(request):
    return render(request, 'car_show.html')

def christmas(request):
    return render(request, 'christmas.html')

def riley_carmack_museum(request):
    return render(request, 'riley_carmack.html')

def coming_soon(request):
    return render(request, 'coming_soon.html')

def culture(request):
    return render(request, 'culture.html')

def events(request):
    return render(request, 'events.html')

def fair(request):
    return render(request, 'fair.html')

def family_fun(request):
    return render(request, 'family_fun.html')

def festivals(request):
    return render(request, 'county_festivals.html')

def food_drink(request):
    businesses = Place.objects.filter(place_page_filter='food')
    context = {
        'businesses': businesses
    }
    return render(request, 'food_drink.html', context)

def history_museums(request):
    return render(request, 'history_museums.html')

def juneteenth(request):
    return render(request, 'juneteenth.html')

def lathrop_festival(request):
    return render(request, 'lathrop_living_history.html')

def lodging(request):
    lodging_places = Place.objects.filter(place_page_filter='lodging')
    context = {
        'businesses': lodging_places
    }
    return render(request, 'lodging.html', context)

def main_st(request):
    return render(request, 'main_st_stroll.html')

def music(request):
    return render(request, 'music.html')

def oak_st(request):
    return render(request, 'oak_st_market.html')

def outdoor_adventure(request):
    return render(request, 'outdoor_adventure.html')

def resources(request):
    all_resources = Place.objects.all()
    context = {
        'resources': all_resources
    }
    return render(request, 'resources.html', context)

def shatto_milk(request):
    return render(request, 'shatto_milk.html')

def shopping_leisure(request):
    shopping_places = Place.objects.filter(place_page_filter='shopping')
    context = {
        'businesses': shopping_places
    }
    return render(request, 'shopping_leisure.html', context)

def tours(request):
    return render(request, 'tours.html')

def golf(request):
    return render(request, 'golf.html')

def hartell_conservation_area(request):
    return render(request, 'hartell_conservation_area.html')

def mcgee_family_conservation(request):
    return render(request, 'mcgee_family_conservation.html')

def smithville_lake(request):
    return render(request, 'smithville_lake.html')

def trice_dedman(request):
    return render(request, 'trice_dedman.html')

def wallace_state_park(request):
    return render(request, 'wallace_state_park.html')