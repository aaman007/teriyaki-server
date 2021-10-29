from django.db.models.signals import post_save
from django.dispatch import receiver

from product.models import Product


@receiver(post_save, sender=Product)
def populate_sku_field(sender, instance: Product, created, **kwargs):
    if created:
        Product.objects.filter(id=instance.id).update(sku=f'P-{str(instance.id).zfill(9)}')
