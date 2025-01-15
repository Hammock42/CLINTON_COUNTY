from django.shortcuts import render
from .models import Thing, FilterType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from static.data.data_lists import thing_categories, cities

# Create your views here.
def thing_list(request):
    things = get_things('recommended', 'all', 'all')
    paginator = Paginator(things, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
        
    context = {
        'things': page_obj,
        'categories_list': thing_categories,
        'cities_list': cities
    }
    
    return render(request, 'things/things.html', context)


def thing_list_filtered(request):
    selected_category = request.GET.get('categories')
    selected_city = request.GET.get('city')
    selected_sort = request.GET.get('sort')
           
    things = get_things(selected_sort, selected_category, selected_city)
    paginator = Paginator(things, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'things': page_obj,
        'categories_list': thing_categories,
        'cities_list': cities,
    }
    
    return render(request, 'things/things.html', context)


def filter_featured_things(things):
    featured = list(things.filter(featured=True))
    non_featured = list(things.filter(featured=False))
    filtered_things = featured + non_featured
    return filtered_things

def get_things(sort_by, category, city):
    things = Thing.objects.all()
    if sort_by == 'az':
        things = things.order_by('name')
    elif sort_by == 'za':
        things = things.order_by('-name')
    if category != 'all':
        things = things.filter(filter_type_list__name__in=[category])
    if city != 'all':
        things = things.filter(city=city)  
    things = filter_featured_things(things)
    return things


def thing_detail(request, thing_slug):
    thing = Thing.objects.get(slug=thing_slug)
    context = {
        'thing': thing
    }
    if thing.internal_page:
        page = f"things/{thing_slug}.html"
        return render(request, page, context)
    return render(request, 'things/thing_detail.html', context)