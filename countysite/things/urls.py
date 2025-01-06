from .views import *
from django.urls import path

app_name = 'things'

urlpatterns = [
    path('', thing_list, name='thing_list'),
    path('filtered/', thing_list_filtered, name='thing_list_filtered'),
    path('<slug:thing_slug>/', thing_detail, name='thing_detail'),
]