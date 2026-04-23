from django.shortcuts import render
from .models import Resource
from static.data.data_lists import resource_categories, cities, subcategories
from django.core.paginator import Paginator

# Create your views here.
def resource_list(request):
    resources = get_resources('recommended', 'all', 'all')
    paginator = Paginator(resources, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'resources': page_obj,
        'categories_list': resource_categories,
        'subcategories_list': subcategories,
        'cities_list': cities
    }
    return render(request, 'resources/resources.html', context)

def filter_featured_resources(resources):
    featured = list(resources.filter(featured=True))
    custom_card = list(resources.filter(featured=False, custom_card=True))
    non_featured = list(resources.filter(featured=False, custom_card=False))
    filtered_resources = featured + custom_card + non_featured
    return filtered_resources

def get_resources(sort_by, category, city):
    resources = Resource.objects.all()
    if sort_by == 'az':
        resources = resources.order_by('name')
    elif sort_by == 'za':
        resources = resources.order_by('-name')
    if category != 'all':
        resources = resources.filter(filter_type_list__name__in=[category])
    if city != 'all':
        resources = resources.filter(city=city)  
    resources = filter_featured_resources(resources)
    return resources

def resource_list_filtered(request):
    selected_category = request.GET.get('categories')
    selected_city = request.GET.get('city')
    selected_sort = request.GET.get('sort')
           
    resources = get_resources(selected_sort, selected_category, selected_city)
    paginator = Paginator(resources, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'resources': page_obj,
        'categories_list': resource_categories,
        'cities_list': cities,
    }
    
    return render(request, 'resources/resources.html', context)

def resource_detail(request, resource_slug):
    resource = Resource.objects.get(slug=resource_slug)
    
    if resource.things_page:
        context = {
            'thing': resource
        }
        if resource.internal_page:
            template = f"things/{resource.slug}.html"
        else:
            template = 'things/thing_detail.html'
        
    elif resource.places_page:
        context = {
            'place': resource
        }
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

def resource_directory(request):
    resources = Resource.objects.all()
    context = {
        'resources': resources,
        'categories_list': resource_categories,
        'subcategories_list': subcategories,
        'cities_list': cities
    }
    return render(request, 'resources/resources_directory.html', context)