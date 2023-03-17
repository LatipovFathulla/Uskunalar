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
    list_display = ['id', 'get_html_photo']

    def get_html_photo(self, object):
        if object.img_uz:
            return mark_safe(f"<img src='{object.img_uz.url}', width=200, height=100>")
        if object.img_ru:
            return mark_safe(f"<img src='{object.img_ru.url}', width=200, height=100>")
        if object.img_en:
            return mark_safe(f"<img src='{object.img_en.url}', width=200, height=100>")

    get_html_photo.short_description = "изб"
