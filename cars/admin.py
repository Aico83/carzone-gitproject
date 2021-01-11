from django.contrib import admin
from . models import Car
from django.utils.html import format_html

# Register your models here.

class CarAdmin(admin.ModelAdmin):
    def image_admin(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.car_photo.url))

    image_admin.short_description = 'Car Image'

    list_display = ('id', 'image_admin', 'car_title', 'city', 'color', 'model', 'year', 'body_style', 'fuel_type', 'is_featured')
    list_display_links = ('id', 'image_admin', 'car_title')
    list_editable = ('is_featured',)
    search_fields = ('id', 'car_title', 'state', 'city', 'year', 'model', 'body_style', 'fuel_type',)
    list_filter = ('city', 'state', 'model', 'body_style', 'fuel_type',)
admin.site.register(Car, CarAdmin)
