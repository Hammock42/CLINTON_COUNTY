from django.contrib import admin
from .models import Place, PlaceType

# Register your models here.    
admin.site.register(Place)
admin.site.register(PlaceType)