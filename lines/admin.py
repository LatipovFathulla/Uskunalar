from django.contrib import admin

from lines.models import LineModel


@admin.register(LineModel)
class LineModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created_at']
    search_fields = ['title']
    list_filter = ['title', 'created_at']
