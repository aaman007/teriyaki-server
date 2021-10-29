from django.contrib import admin

from vendor.models import Vendor


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date', 'modified_date']
    search_fields = ['name']
    filter_horizontal = ['managers']
