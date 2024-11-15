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
    path('arts/', views.arts, name='arts'),
    path('coming_soon/', views.coming_soon, name='coming_soon'),
    path('culture/', views.culture, name='culture'),
    path('events/', views.events, name='events'),
    path('family_fun/', views.family_fun, name='family_fun'),
    path('food_drink/', views.food_drink, name='food_drink'),
    path('history_museums/', views.history_museums, name='history_museums'),
    path('music/', views.music, name='music'),
    path('outdoor_adventure/', views.outdoor_adventure, name='outdoor_adventure'),
    path('place/', views.place, name='place'),
    path('place_alt/', views.place_alt, name='place_alt'),
    path('shopping_leisure/', views.shopping_leisure, name='shopping_leisure'),
    path('tours/', views.tours, name='tours'),
]
