from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from videos.models import VideoModel


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


@admin.register(VideoModel)
class VideoModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'url', 'created_at']
    search_fields = ['title']
    list_filter = ['title', 'created_at']
