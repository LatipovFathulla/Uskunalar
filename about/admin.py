from django.contrib import admin


from about.models import AboutModel, VideoModel


@admin.register(AboutModel)
class AboutModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']
    list_filter = ['title', 'created_at']


@admin.register(VideoModel)
class VideoModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'video']
    search_fields = ['name']
    list_filter = ['name', 'created_at']


