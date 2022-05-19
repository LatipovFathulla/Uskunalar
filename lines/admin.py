from django.contrib import admin
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin

from lines.models import LineModel, LineSpecificationModel, LineCategoryModel, LineTextModel


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


class LineSpecificationModelAdmin(admin.TabularInline):
    model = LineSpecificationModel


@admin.register(LineTextModel)
class LineTextModel(MyTranslationAdmin):
    list_display = ['text', 'created_at']
    search_fields = ['text', 'created_at']
    list_filter = ['text', 'created_at']


@admin.display()
def format_category(obj):
    return mark_safe(obj.category)


@admin.register(LineCategoryModel)
class LineCategoryModel(MyTranslationAdmin):
    list_display = [format_category, 'created_at']
    search_fields = ['category']
    list_filter = ['category', 'created_at']


@admin.register(LineModel)
class LineModelAdmin(MyTranslationAdmin):
    list_display = ['pk', 'title', 'category', 'created_at']
    search_fields = ['title', 'pk']
    list_filter = ['title', 'created_at']

    inlines = [LineSpecificationModelAdmin]
