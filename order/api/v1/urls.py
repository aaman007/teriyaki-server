from django.urls import path

from order.api.v1.views import OrderListAPIView, OrderRetrieveAPIView

app_name = 'order-api-v1'

urlpatterns = [
    path('orders/', OrderListAPIView.as_view(), name='order_list'),
    path('orders/<str:sku>/', OrderRetrieveAPIView.as_view(), name='order_retrieve')
]
