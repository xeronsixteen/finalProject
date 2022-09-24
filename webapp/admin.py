from django.contrib import admin

from webapp.models import Photo, Album


# Register your models here.

class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'description']
    list_display_links = ['description']
    search_fields = ['user', 'description']
    fields = ['image', 'description']
    # readonly_fields = ['created_at', 'updated_at']
    # filter_horizontal = ['category']


class AlbumAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']


admin.site.register(Photo, PhotoAdmin)
admin.site.register(Album, AlbumAdmin)
from django.contrib import admin

# Register your models here.
