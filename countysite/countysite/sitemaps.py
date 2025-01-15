from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from places.models import Place
from things.models import Thing
from events.models import Event
from resources.models import Resource


class StaticViewSitemap(Sitemap):
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return ['index', 'about', 'coming_soon', 'privacy_policy', 'legal_statement', 'events:event_list', 'places:place_list', 'things:thing_list', 'resources:resource_list']

    def location(self, item):
        return reverse(item)
    
class PlaceSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.8

    def items(self):
        return Place.objects.all()

    def lastmod(self, obj):
        return obj.updated_at
    
class ThingSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.8

    def items(self):
        return Thing.objects.all()

    def lastmod(self, obj):
        return obj.updated_at
    
    
class EventSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.8

    def items(self):
        return Event.objects.all()

    def lastmod(self, obj):
        return obj.updated_at
    
class ResourceSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.8

    def items(self):
        return Resource.objects.all()
    
    def lastmod(self, obj):
        return obj.updated_at
    