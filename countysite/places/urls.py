from .views import *
from django.urls import path

app_name = 'places'

urlpatterns = [
    path('', place_list, name='place_list'),
    path('filtered/', filtered_place_list, name='filtered_place_list'),
    path('<slug:place_slug>/', place_detail, name='place_detail'),
]