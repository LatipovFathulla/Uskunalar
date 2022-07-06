from django.contrib import admin

from gallery.models import GalleryModel, GalleyImageModel


class GalleryImageModelAdmin(admin.TabularInline):
    model = GalleyImageModel


@admin.register(GalleryModel)
class GalleryModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_descriptions', 'created_at']
    search_fields = ['title']
    list_filter = ['title', 'created_at']
    inlines = [GalleryImageModelAdmin]
