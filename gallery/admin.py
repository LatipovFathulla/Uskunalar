from django.contrib import admin

from gallery.models import GalleryModel


@admin.register(GalleryModel)
class GalleryModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'short_descriptions', 'created_at']
    search_fields = ['title']
    list_filter = ['title', 'created_at']
