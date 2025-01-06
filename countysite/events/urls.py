from .views import *
from django.urls import path

app_name = 'events'

urlpatterns = [
    path('', event_list, name='event_list'),
    path('filtered/', filtered_event_list, name='filtered_event_list'),
    path('<slug:event_slug>/', event_detail, name='event_detail'),
]