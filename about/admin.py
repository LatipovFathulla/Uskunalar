from django.contrib import admin


from about.models import AboutModel, ContactModel


@admin.register(AboutModel)
class AboutModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']
    list_filter = ['title', 'created_at']


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'message', 'created_at']
    search_fields = ['name', 'phone']
    list_filter = ['name', 'phone', 'created_at']



