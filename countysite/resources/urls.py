from .views import *
from django.urls import path

app_name = 'resources'

urlpatterns = [
    path('', resource_list, name='resource_list'),
    path('filtered/', resource_list_filtered, name='resource_list_filtered'),
    path('<slug:resource_slug>/', resource_detail, name='resource_detail'),
]