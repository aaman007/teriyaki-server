from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import AbstractTimestampModel


class Vendor(AbstractTimestampModel):
    name = models.CharField(verbose_name=_('Name'), max_length=255)
    address = models.TextField(verbose_name=_('Address'))
    managers = models.ManyToManyField(
        verbose_name=_('Managers'),
        to=settings.AUTH_USER_MODEL,
        related_name='vendors'
    )

    class Meta:
        verbose_name = _('Vendor')
        verbose_name_plural = _('Vendors')

    def __str__(self):
        return self.name
