from django.contrib import admin
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin

from works.models import WorkModel, WorkSpecificationsModel, WorkImageModel


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


class WorkSpecificationsModelAdmin(admin.TabularInline):
    model = WorkSpecificationsModel


class WorkImageModelAdmin(admin.TabularInline):
    model = WorkImageModel


@admin.display()
def format_desc(obj):
    return mark_safe(obj.short_descriptions)


@admin.register(WorkModel)
class WorkModelAdmin(MyTranslationAdmin):
    list_display = ['pk', 'title', 'image', format_desc, 'created_at']
    search_fields = ['title', 'pk']
    list_filter = ['title', 'created_at']

    inlines = [WorkSpecificationsModelAdmin, WorkImageModelAdmin]
