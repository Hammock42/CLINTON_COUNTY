from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    featured = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    schedule = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to='event_img/', blank=True, null=True)
    filter_type_list = models.ManyToManyField('things.FilterType', related_name='event_type_filters', blank=True)
    external_link = models.URLField(blank=True)
    internal_page = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('events:event_detail', kwargs={'event_slug': self.slug})
    
    def get_full_address(self):
        return f'{self.address}, {self.city}, MO'
    
    def get_date_range(self):
        return f'{self.start_date} - {self.end_date}'
    
    def get_type_filters(self):
        return ', '.join([str(filter_type) for filter_type in self.filter_type_list.all()])