from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import AbstractTimestampModel


class OrderedItem(models.Model):
    product = models.ForeignKey(
        verbose_name=_('Product'),
        to='product.Product',
        related_name='ordered_items',
        on_delete=models.CASCADE
    )
    order = models.ForeignKey(
        verbose_name=_('Order'),
        to='Order',
        related_name='ordered_items',
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(verbose_name=_('Quantity'))
    cost = models.FloatField(verbose_name=_('Cost'), default=0.0)

    class Meta:
        verbose_name = _('Ordered Item')
        verbose_name_plural = _('Ordered Items')

    @property
    def amount(self):
        return self.product.price * self.quantity


class Order(AbstractTimestampModel):
    class Status(models.TextChoices):
        PENDING = 'pending', _('Pending')
        RECEIVED = 'received', _('Received')
        IN_PROGRESS = 'in progress', _('In Progress')
        DELIVERED = 'delivered', _('Delivered')
        CANCELED = 'canceled', _('Canceled')

    user = models.ForeignKey(
        verbose_name=_('User'),
        to=settings.AUTH_USER_MODEL,
        related_name='orders',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    sku = models.CharField(verbose_name=_('SKU'), max_length=50)
    status = models.CharField(verbose_name=_('Status'), choices=Status.choices, max_length=40)
    address = models.ForeignKey(
        verbose_name=_('Address'),
        to='accounts.Address',
        related_name='orders',
        on_delete=models.SET_NULL,
        null=True
    )
    phone_number = models.CharField(verbose_name=_('Phone Number'), max_length=15, blank=True)
    sub_total = models.FloatField(verbose_name=_('Sub Total'), default=0.0)
    delivery_charge = models.FloatField(verbose_name=_('Delivery Charge'), default=0.0)

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return self.sku

    @property
    def total_cost(self):
        return self.sub_total + self.delivery_charge
