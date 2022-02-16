from django.contrib import admin

from works.models import WorkModel, WorkSpecificationsModel, WorkImageModel


class WorkSpecificationsModelAdmin(admin.TabularInline):
    model = WorkSpecificationsModel


class WorkImageModelAdmin(admin.TabularInline):
    model = WorkImageModel


@admin.register(WorkModel)
class WorkModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'short_descriptions', 'created_at']
    search_fields = ['title']
    list_filter = ['title', 'created_at']

    inlines = [WorkSpecificationsModelAdmin, WorkImageModelAdmin]
