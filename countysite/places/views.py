from django.shortcuts import render
from .models import Place
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from static.data.data_lists import place_categories, cities

# Create your views here.
def place_list(request):
    places_query = Place.objects.all().order_by('?')
    places = filter_featured_places(places_query)
    paginator = Paginator(places, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'places': page_obj,
        'categories_list': place_categories,
        'cities_list': cities
    }
    return render(request, 'places/places.html', context)

def filtered_place_list(request):
    selected_category = request.GET.get('categories')
    selected_city = request.GET.get('city')
    selected_sort = request.GET.get('sort')
    
    if selected_sort == 'az':
        places_query = Place.objects.all().order_by('name')
    elif selected_sort == 'za':
        places_query = Place.objects.all().order_by('-name')
    else:
        places_query = Place.objects.all().order_by('?')
    if selected_category != 'all':
        places_query = places_query.filter(filter_subtype_list__name__in=[selected_category])
    if selected_city != 'all':
        places_query = places_query.filter(city=selected_city)
        
    places = filter_featured_places(places_query)
    paginator = Paginator(places, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'places': page_obj,
        'categories_list': place_categories,
        'cities_list': cities
    }
    return render(request, 'places/places.html', context)

def place_detail(request, place_slug):
    place = Place.objects.get(slug=place_slug)
    context = {
        'place': place
    }
    return render(request, 'places/place_detail.html', context)

def filter_featured_places(places):
    featured_places = list(places.filter(featured=True))
    non_featured_places = list(places.filter(featured=False))
    shuffled_places = featured_places + non_featured_places
    return shuffled_places
