from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Place(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    featured = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    external_website = models.URLField(blank=True, null=True)
    internal_page = models.BooleanField(default=False)
    email = models.EmailField(blank=True, null=True)
    image = models.ImageField(upload_to='place_img/', blank=True, null=True)
    operation_hours = models.CharField(max_length=100, blank=True, null=True)
    filter_type_list = models.ManyToManyField('things.FilterType', related_name='place_type_filters', blank=True)
    filter_subtype_list = models.ManyToManyField('things.FilterSubType', related_name='place_subtype_filters', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('places:place_detail', kwargs={'place_slug': self.slug})
    
    def get_filter_types(self):
        return ', '.join([filter_type.name for filter_type in self.filter_type_list.all()])
    
    def get_filter_subtypes(self):
        return ', '.join([filter_subtype.name for filter_subtype in self.filter_subtype_list.all()])
    
    def get_full_address(self):
        return f'{self.address}, {self.city}, MO'