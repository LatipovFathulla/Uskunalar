from django.contrib import admin

from works.models import WorkModel


@admin.register(WorkModel)
class WorkModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'created_at']
    search_fields = ['title']
    list_filter = ['title', 'created_at']