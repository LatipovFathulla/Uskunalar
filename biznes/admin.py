from django.contrib import admin
from django.utils.safestring import mark_safe

from biznes.models import BiznesModel, BiznesImageModel
from home.admin import MyTranslationAdmin


class BiznesImageModelAdmin(admin.TabularInline):
    model = BiznesImageModel


@admin.display()
def format_title(obj):
    return mark_safe(obj.title)


@admin.register(BiznesModel)
class BiznesModelAdmin(MyTranslationAdmin):
    list_display = ['pk', format_title, 'image', 'created_at']
    search_fields = ['title', 'pk']
    list_filter = ['title', 'created_at']

    inlines = [BiznesImageModelAdmin]
