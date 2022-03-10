from django.contrib import admin

from orders.models import OrderModel


@admin.register(OrderModel)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone',]
    search_fields = ['name', 'phone', 'products']
