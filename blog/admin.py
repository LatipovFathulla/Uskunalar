from django.contrib import admin
from django.utils.safestring import mark_safe

from blog.models import BlogModel
from home.admin import MyTranslationAdmin


@admin.display()
def format_desc(obj):
    return mark_safe(obj.smart_text)


@admin.register(BlogModel)
class BlogModelAdmin(MyTranslationAdmin):
    list_display = ['pk', 'title', format_desc, 'created_at']
    search_fields = ['title', 'pk']
    list_filter = ['title']
