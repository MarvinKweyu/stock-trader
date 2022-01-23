from django.contrib import admin
from localstore.models import Product, Reorder


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin interface for Product
    """
    list_display = ('name', 'price',
                    'inventory', 're_order_level')
    search_fields = ('name',)


@admin.register(Reorder)
class ReorderAdmin(admin.ModelAdmin):
    """
    Admin interface for Reorder
    """
    list_display = ('product', 'quantity',
                    'status', 'reorder_date')
    list_filter = ('status', 'reorder_date')
    # search_fields = ('name')
