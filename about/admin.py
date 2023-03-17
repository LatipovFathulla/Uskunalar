from django.contrib import admin
from django.utils.safestring import mark_safe

from about.models import AboutModel, RequestsModel, TransModel
from home.admin import MyTranslationAdmin


@admin.display()
def format_title(obj):
    return mark_safe(obj.title)


@admin.register(AboutModel)
class AboutModelAdmin(MyTranslationAdmin):
    list_display = ['pk', format_title, 'created_at']
    search_fields = ['title']
    list_filter = ['title', 'created_at']


@admin.register(RequestsModel)
class RequestsModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'message', 'created_at']
    search_fields = ['name', 'phone']
    list_filter = ['name', 'phone', 'created_at']


@admin.register(TransModel)
class TransModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'img_uz', 'img_ru', 'img_en']
