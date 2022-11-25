from django.db.models import signals
from django.dispatch import receiver
from .models import Store

# pre save
@receiver(signals.pre_save ,sender=Store)
def quantitychecker(sender, instance, using, **kwargs):

    try:
        product = Store.objects.get(id=instance.id)

        if instance.quantity > product.quantity:
            raise Exception("Out of Stock")
    except Store.DoesNotExist:
        pass

# visit apps.py line number 8 ! important