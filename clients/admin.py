from django.contrib import admin
from django.utils.safestring import mark_safe

from clients.models import ClientModel


@admin.register(ClientModel)
class ClientModelAdmin(admin.ModelAdmin):
    list_display = ['get_html_photo', 'created_at']

    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}', width=200, height=100>")

    get_html_photo.short_description = "партнеры"