from rest_framework import serializers

from localstore.models import Product, Reorder

# ReorderItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "price", "inventory", "re_order_level")


class ReorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reorder
        fields = ("id", "product", "quantity", "status", "reorder_date")
