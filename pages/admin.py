from django.contrib import admin
from .models import Team
from django.utils.html import format_html
# Register your models here.


class TeamAdmin(admin.ModelAdmin):
    def image_admin(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.photo.url))

    image_admin.short_description = 'Photo'

    list_display = ('id','image_admin','first_name','designation','created_date')
    list_display_links = ('id','image_admin','first_name',)
    search_fields = ('first_name','last_name','designation')
    list_filter = ('designation',)


admin.site.register(Team, TeamAdmin)
