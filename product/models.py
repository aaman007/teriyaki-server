from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import AbstractTimestampModel
from core.fields import TitleField


class Category(AbstractTimestampModel):
    name = TitleField(verbose_name=_('Name'))
    description = models.TextField(verbose_name=_('Description'))
    parent = models.ForeignKey(
        verbose_name=_('Parent'),
        to='self',
        related_name='children',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name


class Product(AbstractTimestampModel):
    vendor = models.ForeignKey(
        verbose_name=_('Vendor'),
        to='vendor.Vendor',
        related_name='products',
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        verbose_name=_('Category'),
        to='Category',
        related_name='products',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    name = TitleField(verbose_name=_('Name'))
    description = models.TextField(verbose_name=_('Description'))
    price = models.FloatField(verbose_name=_('Price'), null=True, blank=True)
    stocks = models.PositiveIntegerField(verbose_name=_('Stocks'), default=0)
    sku = models.CharField(verbose_name=_('SKU'), max_length=50)
    rating = models.FloatField(verbose_name=_('Rating'), null=True, blank=True)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.name


class Review(AbstractTimestampModel):
    user = models.ForeignKey(
        verbose_name=_('User'),
        to=settings.AUTH_USER_MODEL,
        related_name='reviews',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        verbose_name=_('Product'),
        to='Product',
        related_name='reviews',
        on_delete=models.CASCADE
    )

    rating = models.FloatField(verbose_name=_('Rating'), default=0.0)
    description = models.TextField(verbose_name=_('Description'))

    class Meta:
        verbose_name = _('Review')
        verbose_name_plural = _('Reviews')
        unique_together = ('user', 'product')

    def __str__(self):
        return self.description[:20]
