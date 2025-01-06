from django.shortcuts import render
from .models import Thing, FilterType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from static.data.data_lists import thing_categories, cities

# Create your views here.
def thing_list(request):
    things_query = Thing.objects.all().order_by('?')
    things = filter_featured_things(things_query)
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
        
    if selected_sort == 'az':
        things_query = Thing.objects.all().order_by('name')
    elif selected_sort == 'za':
        things_query = Thing.objects.all().order_by('-name')
    else:
        things_query = Thing.objects.all().order_by('?')
        
    if selected_category != 'all':
        things_query = things_query.filter(filter_type_list__name__in=[selected_category])
    if selected_city != 'all':
        things_query = things_query.filter(city=selected_city)
            
    things = filter_featured_things(things_query)
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


def thing_detail(request, thing_slug):
    thing = Thing.objects.get(slug=thing_slug)
    context = {
        'thing': thing
    }
    if thing.internal_page:
        page = f"things/{thing_slug}.html"
        return render(request, page, context)
    return render(request, 'things/thing_detail.html', context)