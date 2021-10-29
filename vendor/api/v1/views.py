from rest_framework.generics import ListAPIView, RetrieveAPIView

from vendor.api.v1.serializers import VendorSerializer
from vendor.models import Vendor


class VendorListAPIView(ListAPIView):
    serializer_class = VendorSerializer

    def get_queryset(self):
        return Vendor.objects.all()


class VendorRetrieveAPIView(RetrieveAPIView):
    serializer_class = VendorSerializer

    def get_queryset(self):
        return Vendor.objects.all()
