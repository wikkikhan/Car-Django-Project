from django.contrib import admin
from .models import Team
from django.utils.html import format_html


class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}"  width="40px" style="border-radius: 50px"/>'.format(object.image.url))
    
    thumbnail.short_description = 'Photo'

    list_display = ('id','thumbnail', 'firstName' , 'Designation', 'date')
    list_display_links = ('id', 'firstName')
    search_fields = ('firstName', 'Designation')
    list_filter = ('Designation',)

admin.site.register(Team, TeamAdmin)
