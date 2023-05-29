from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'brand', 'warranty', 'seller', 'price', 'is_liked')
    list_filter = ('category', 'brand', 'warranty', 'seller')
    search_fields = ('name', 'category', 'brand')
