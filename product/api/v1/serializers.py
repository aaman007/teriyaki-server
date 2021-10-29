from rest_framework import serializers

from accounts.api.v1.serializers import UserSerializer
from vendor.api.v1.serializers import VendorSerializer
from product.models import Category, Review, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id', 'parent', 'name', 'description'
        ]


class ProductSerializer(serializers.ModelSerializer):
    vendor = VendorSerializer()
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = [
            'sku', 'vendor', 'category', 'name', 'description',
            'price', 'stocks', 'rating', 'created_date'
        ]


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Review
        fields = [
            'id', 'user', 'rating', 'description'
        ]
