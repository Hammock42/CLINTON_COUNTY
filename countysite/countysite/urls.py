"""
URL configuration for countysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('abbey/', views.abbey, name='abbey'),
    path('about/', views.about, name='about'),
    path('antique_show/', views.antique_show, name='antique_show'),
    path('arts/', views.arts, name='arts'),
    path('cameron_depot_museum/', views.cameron_depot_museum, name='cameron_depot_museum'),
    path('car_show/', views.car_show, name='car_show'),
    path('christmas/', views.christmas, name='christmas'),
    path('coming_soon/', views.coming_soon, name='coming_soon'),
    path('culture/', views.culture, name='culture'),
    path('events/', views.events, name='events'),
    path('fair/', views.fair, name='fair'),
    path('family_fun/', views.family_fun, name='family_fun'),
    path('festivals/', views.festivals, name='festivals'),
    path('food_drink/', views.food_drink, name='food_drink'),
    path('history_museums/', views.history_museums, name='history_museums'),
    path('juneteenth/', views.juneteenth, name='juneteenth'),
    path('lathrop_festival/', views.lathrop_festival, name='lathrop_festival'),
    path('lodging/', views.lodging, name='lodging'),
    path('main_st/', views.main_st, name='main_st'),
    path('music/', views.music, name='music'),
    path('oak_st/', views.oak_st, name='oak_st'),
    path('outdoor_adventure/', views.outdoor_adventure, name='outdoor_adventure'),
    path('resources/', views.resources, name='resources'),
    path('riley_carmack_museum/', views.riley_carmack_museum, name='riley_carmack_museum'),
    path('shatto_milk/', views.shatto_milk, name='shatto_milk'),
    path('shopping_leisure/', views.shopping_leisure, name='shopping_leisure'),
    path('tours/', views.tours, name='tours'),
    path('hartell_conservation_area/', views.hartell_conservation_area, name='hartell_conservation_area'),
    path('golf/', views.golf, name='golf'),
    path('mcgee_family_conservation/', views.mcgee_family_conservation, name='mcgee_family_conservation'),
    path('smithville_lake/', views.smithville_lake, name='smithville_lake'),
    path('trice_dedman/', views.trice_dedman, name='trice_dedman'),
    path('wallace_state_park/', views.wallace_state_park, name='wallace_state_park'),
]
