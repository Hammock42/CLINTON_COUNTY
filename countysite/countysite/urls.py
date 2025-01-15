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
from django.views.generic.base import TemplateView
from django.contrib.sitemaps.views import sitemap
from .sitemaps import *

sitemaps = {
    'static': StaticViewSitemap,
    'places': PlaceSitemap,
    'things': ThingSitemap,
    'events': EventSitemap,
    'resources': ResourceSitemap,
}

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt/', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('coming_soon/', views.coming_soon, name='coming_soon'),
    path('legal_statement/', views.legal_statement, name='legal_statement'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('events-to-enjoy/', include('events.urls')),
    path('places-to-stay/', include('places.urls')),
    path('things-to-do/', include('things.urls')),
    path('resources-to-use/', include('resources.urls')),
]
