from django.db import models
from django.urls import reverse

place_page_choices = (
    ('food', 'Food'),
    ('lodging', 'Lodging'),
    ('shopping', 'Shopping'),
    ('all', 'All'),
)

class PlaceType(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('place_type', kwargs={'slug': self.slug})

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    place_type_list = models.ManyToManyField('PlaceType', related_name='places', blank=True)
    place_page_filter = models.CharField(max_length=20, choices=place_page_choices, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    image = models.ImageField(upload_to='places/images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('place_detail', kwargs={'slug': self.slug})
    
    def get_place_types(self):
        return ', '.join([place_type.name for place_type in self.place_type_list.all()])