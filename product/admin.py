from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from product.models import Category, Product, Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'parent', 'modified_date']
    readonly_fields = ['created_date', 'modified_date']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'sku', 'name', 'category', 'vendor', 'price', 'stocks', 'rating']
    readonly_fields = ['sku', 'created_date', 'modified_date']
    fieldsets = [
        [None, {'fields': ['vendor', 'category']}],
        [_('Info'), {'fields': ['sku', 'name', 'description']}],
        [_('Extras'), {'fields': ['price', 'stocks', 'rating']}],
        [_('Important Dates'), {'fields': ['created_date', 'modified_date']}]
    ]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'rating', 'description']
    readonly_fields = ['created_date', 'modified_date']


