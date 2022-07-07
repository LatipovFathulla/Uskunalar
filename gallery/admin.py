from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from gallery.models import GalleryModel, GalleyImageModel


class MyTranslationAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class GalleryImageModelAdmin(admin.TabularInline):
    model = GalleyImageModel


@admin.register(GalleryModel)
class GalleryModelAdmin(MyTranslationAdmin):
    list_display = ['pk', 'title', 'short_descriptions', 'created_at']
    search_fields = ['title']
    list_filter = ['title', 'created_at']
    inlines = [GalleryImageModelAdmin]
