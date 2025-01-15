from django.shortcuts import render
from .models import Resource
from static.data.data_lists import resource_categories, cities, subcategories
from things.models import Thing
from places.models import Place
import random
from itertools import chain

# Create your views here.
def resource_list(request):
    resources = Resource.objects.all()
    places = Place.objects.all()
    # only show things that filter_types are in the categories_list
    things = Thing.objects.all()
    all_resources = list(chain(resources, places, things))
    random.shuffle(all_resources)
    
    context = {
        'resources': all_resources,
        'categories_list': resource_categories,
        'subcategories_list': subcategories,
        'cities_list': cities
    }
    return render(request, 'resources/resources.html', context)

def resource_detail(request, resource_slug):
    resource = None
    thing = None
    place = None

    try:
        resource = Resource.objects.get(slug=resource_slug)
    except Resource.DoesNotExist:
        try:
            resource = Thing.objects.get(slug=resource_slug)
        except Thing.DoesNotExist:
            try:
                resource = Place.objects.get(slug=resource_slug)
            except Place.DoesNotExist:
                pass

    context = {
        'resource': resource
    }
    return render(request, 'resources/resource_detail.html', context)
