from django.contrib import admin


from about.models import AboutModel, RequestsModel


@admin.register(AboutModel)
class AboutModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']
    list_filter = ['title', 'created_at']


@admin.register(RequestsModel)
class RequestsModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'message', 'created_at']
    search_fields = ['name', 'phone']
    list_filter = ['name', 'phone', 'created_at']



