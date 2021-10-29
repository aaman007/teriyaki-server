from rest_framework import serializers

from accounts.api.v1.serializers import AddressSerializer
from product.api.v1.serializers import ProductSerializer
from order.models import Order, OrderedItem


class OrderedItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderedItem
        fields = [
            'product', 'quantity', 'cost'
        ]


class OrderSerializer(serializers.ModelSerializer):
    ordered_items = OrderedItemSerializer(many=True)
    address = AddressSerializer()

    class Meta:
        model = Order
        fields = [
            'sku', 'status', 'address', 'phone_number', 'ordered_items', 'sub_total',
            'delivery_charge', 'total_cost', 'created_date', 'modified_date'
        ]
        read_only_fields = ['sku', 'status', 'sub_total', 'delivery_charge']
