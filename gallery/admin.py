from django.contrib import admin
from .models import Image, Location, Category

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal =('Location',)

admin.site.register(Image)
admin.site.register(Location)
admin.site.register(Category)
