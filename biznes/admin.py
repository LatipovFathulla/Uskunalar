from django.contrib import admin

from biznes.models import BiznesModel, BiznesImageModel
from home.admin import MyTranslationAdmin


class BiznesImageModelAdmin(admin.TabularInline):
    model = BiznesImageModel


@admin.register(BiznesModel)
class BiznesModelAdmin(MyTranslationAdmin):
    list_display = ['pk', 'title', 'image', 'created_at']
    search_fields = ['title', 'pk']
    list_filter = ['title', 'created_at']

    inlines = [BiznesImageModelAdmin]
