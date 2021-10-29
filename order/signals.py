from django.db.models.signals import post_save
from django.dispatch import receiver

from order.models import Order


@receiver(post_save, sender=Order)
def populate_sku_field(sender, instance: Order, created, **kwargs):
    if created:
        Order.objects.filter(id=instance.id).update(sku=f'O-{str(instance.id).zfill(12)}')
