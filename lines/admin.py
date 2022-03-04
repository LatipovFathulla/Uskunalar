from django.contrib import admin

from lines.models import LineModel, LineSpecificationModel, LineCategoryModel


class LineSpecificationModelAdmin(admin.TabularInline):
    model = LineSpecificationModel


@admin.register(LineCategoryModel)
class LineCategoryModel(admin.ModelAdmin):
    list_display = ['category', 'created_at']
    search_fields = ['category']
    list_filter = ['category', 'created_at']


@admin.register(LineModel)
class LineModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'description', 'created_at']
    search_fields = ['title']
    list_filter = ['title', 'created_at']

    inlines = [LineSpecificationModelAdmin]