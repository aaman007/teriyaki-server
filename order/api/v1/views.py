from django.http import Http404
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from core.api.permissions import IsObjectOwner
from order.api.v1.serializers import OrderSerializer
from order.models import Order


class OrderListAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer
    pagination_class = None

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrderRetrieveAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsObjectOwner]
    serializer_class = OrderSerializer

    def get_object(self):
        sku = self.kwargs.get('sku')
        try:
            order = Order.objects.get(sku=sku)
            self.check_object_permissions(self.request, order.user)
            return order
        except PermissionDenied:
            return self.permission_denied(self.request)
        except (Order.DoesNotExist, Exception):
            raise Http404


