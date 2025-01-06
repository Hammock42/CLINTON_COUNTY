from django.contrib import admin
from .models import Thing, FilterType, FilterSubType

# Register your models here.
admin.site.register(Thing)
admin.site.register(FilterType)
admin.site.register(FilterSubType)

""" @admin.register(Thing)
class ThingAdmin(admin.ModelAdmin):
    list_display = [
        'name', 
        'slug', 
        'featured',
        'description',
        'address',
        'city',
        'phone_number',
        'external_website',
        'internal_page',
        'email',
        'image',
        'operation_hours',
        ] """