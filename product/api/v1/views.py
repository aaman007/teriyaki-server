from rest_framework.generics import ListAPIView, RetrieveAPIView

from product.api.v1.serializers import CategorySerializer, ProductSerializer, ReviewSerializer
from product.models import Category, Product, Review


class CategoryListAPIView(ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()


class CategoryRetrieveAPIView(RetrieveAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()


class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()


class ProductRetrieveAPIView(RetrieveAPIView):
    serializer_class = ProductSerializer
    lookup_field = 'sku'

    def get_queryset(self):
        return Product.objects.all()


class ReviewListAPIView(ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(product__sku=self.kwargs.get('product_sku'))
