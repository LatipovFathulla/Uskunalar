from django.contrib import admin

from videos.models import VideoModel


@admin.register(VideoModel)
class VideoModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'created_at']
    search_fields = ['title']
    list_filter = ['title', 'created_at']
