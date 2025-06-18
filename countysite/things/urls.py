from .views import *
from django.urls import path

app_name = 'things'

urlpatterns = [
    path('', thing_list, name='thing_list'),
    path('thing_template_page/', thing_template_page, name='thing_template_page'),
    path('filtered/', thing_list_filtered, name='thing_list_filtered'),
    path('<slug:thing_slug>/', thing_detail, name='thing_detail'),
]