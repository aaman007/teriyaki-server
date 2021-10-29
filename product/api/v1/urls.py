from django.urls import path

from product.api.v1.views import (
    CategoryListAPIView,
    CategoryRetrieveAPIView,
    ProductListAPIView,
    ProductRetrieveAPIView,
    ReviewListAPIView
)

app_name = 'product-api-v1'

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryRetrieveAPIView.as_view(), name='category_retrieve'),
    path('products/', ProductListAPIView.as_view(), name='product_list'),
    path('products/<str:sku>/', ProductRetrieveAPIView.as_view(), name='product_retrieve'),
    path('products/<str:product_sku>/reviews/', ReviewListAPIView.as_view(), name='review_list')
]
