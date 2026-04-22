from django.shortcuts import render
from .models import Resource
from static.data.data_lists import resource_categories, cities, subcategories
import random
from itertools import chain
from things.views import thing_detail
from places.views import place_detail

# Create your views here.
def resource_list(request):
    all_resources = Resource.objects.all()
    
    
    context = {
        'resources': all_resources,
        'categories_list': resource_categories,
        'subcategories_list': subcategories,
        'cities_list': cities
    }
    return render(request, 'resources/resources.html', context)

def resource_detail(request, resource_slug):
    resource = Resource.objects.get(slug=resource_slug)
    
    if resource.things_page:
        if resource.internal_page:
            template = f"things/{resource.slug}.html"
        else:
            template = 'things/thing_detail.html'
        
    elif resource.places_page:
        if resource.internal_page:
            template = f"places/{resource.slug}.html"
        else:
            template = 'places/place_detail.html'
        
    else:
        template = 'resources/resource_detail.html'
        
    context = {
        'resource': resource
    }
        
    return render(request, template, context)
