from django.shortcuts import render
from .models import Event
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from static.data.data_lists import event_categories, cities
import datetime

# Create your views here.
def event_list(request):
    all_events = Event.objects.all()
    events = filter_featured_events(all_events)
    p = Paginator(events, 8)
    page = request.GET.get('page')
    events = p.get_page(page)
    context = {
        'events': events,
        'categories_list': event_categories,
        'cities_list': cities
    }
    return render(request, 'events/events.html', context)

def filtered_event_list(request):
    event_category = request.GET.get('categories')
    event_city = request.GET.get('city')
    event_sort = request.GET.get('sort')
    
    if event_sort == 'az':
        events = Event.objects.all().order_by('name')
    elif event_sort == 'za':
        events = Event.objects.all().order_by('-name')
    elif event_sort == 'past':
        events = Event.objects.all().filter(end_date__lt=datetime.date.today()).order_by('-start_date')
    elif event_sort == 'upcoming':
        events = Event.objects.all().filter(end_date__gte=datetime.date.today()).order_by('start_date')
    else:
        events = Event.objects.all()
        
    if event_category != 'all':
        events = events.filter(filter_type_list__name__in=[event_category])
    if event_city != 'all':
        events = events.filter(city=event_city)
    events = filter_featured_events(events)
    p = Paginator(events, 8)
    page = request.GET.get('page')
    events = p.get_page(page)
    context = {
        'events': events,
        'categories_list': event_categories,
        'cities_list': cities
    }
    return render(request, 'events/events.html', context)
    

def event_detail(request, event_slug):
    event = Event.objects.get(slug=event_slug)
    context = {
        'event': event
    }
    if event.internal_page:
        page = f"events/{event_slug}.html"
        return render(request, page, context)
    return render(request, 'events/event_detail.html', context)

def filter_featured_events(events):
    featured = list(events.filter(featured=True))
    non_featured = list(events.filter(featured=False))
    filtered_events = featured + non_featured
    return filtered_events
