from django.contrib import admin

from blog.models import BlogModel
from home.admin import MyTranslationAdmin


@admin.register(BlogModel)
class BlogModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'smart_text', 'created_at']
    search_fields = ['title']
    list_filter = ['title']
