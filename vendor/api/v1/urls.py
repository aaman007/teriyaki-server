from django.urls import path

from vendor.api.v1.views import VendorListAPIView, VendorRetrieveAPIView

app_name = 'vendor-api-v1'

urlpatterns = [
    path('vendors/', VendorListAPIView.as_view(), name='vendor_list'),
    path('vendors/<int:pk>/', VendorRetrieveAPIView.as_view(), name='vendor_retrieve')
]
