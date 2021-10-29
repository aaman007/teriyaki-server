from django.contrib import admin

from order.models import OrderedItem, Order


@admin.register(OrderedItem)
class OrderedItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'order', 'quantity', 'cost']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'sku', 'user', 'phone_number', 'status', 'total_cost', 'created_date', 'modified_date'
    ]
    readonly_fields = ['sku', 'created_date', 'modified_date']
