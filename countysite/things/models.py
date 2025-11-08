from django.db import models
from django.urls import reverse
import pillow_avif

# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    featured = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    external_website = models.URLField(blank=True, null=True)
    internal_page = models.BooleanField(default=False)
    custom_card = models.BooleanField(default=False)
    email = models.EmailField(blank=True, null=True)
    image = models.ImageField(upload_to='thing_img/', blank=True, null=True)
    image_alt = models.CharField(max_length=100, blank=True, null=True)
    operation_hours = models.CharField(max_length=100, blank=True, null=True)
    filter_type_list = models.ManyToManyField('FilterType', related_name='type_filters', blank=True)
    filter_subtype_list = models.ManyToManyField('FilterSubType', related_name='subtype_filters', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Things"

    def __str__(self):
        return str(self.name)
    
    def get_absolute_url(self):
        return reverse('things:thing_detail', kwargs={'thing_slug': self.slug})
    
    def get_filter_types(self):
        return ', '.join([filter_type.name for filter_type in self.filter_type_list.all()])
    
    def get_filter_subtypes(self):
        return ', '.join([filter_subtype.name for filter_subtype in self.filter_subtype_list.all()])
    
    def get_full_address(self):
        return f'{self.address}, {self.city}, MO'
    
    def get_operation_hours(self):
        return self.operation_hours.split(';')
    
    

class FilterType(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class FilterSubType(models.Model):
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name