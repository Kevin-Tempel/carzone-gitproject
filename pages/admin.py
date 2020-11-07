from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Team
from django.utils.html import format_html


# Register your models here.
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html(f'<img src="{object.photo.url}" width="40" style="border-radius: 50%;" />')

    thumbnail.short_description = 'Photo'

    list_display        = ('id', 'thumbnail', 'first_name', 'designation', 'created_date')
    list_display_links  = ('id', 'thumbnail', 'first_name')
    search_fields       = ('first_name', 'last_name', 'designation')
    list_filter         = ('designation',)
    class Meta:
        model = Team
        fields = '__all__'
