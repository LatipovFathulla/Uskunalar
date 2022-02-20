from django.contrib import admin

from biznes.models import BiznesModel


@admin.register(BiznesModel)
class BiznesModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'created_at']
    search_fields = ['title']
    list_filter = ['title', 'created_at']
