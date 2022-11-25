
from django.db import models




class Store(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    def __str__(self):
        return self.product_name


# write siganls after Model class
# go to signals.py for signal
# @receiver(signals.pre_save ,sender=Store)
# def quantitychecker(sender, instance, using, **kwargs):
#     product = Store.objects.get(id=instance.id)
#
#     if instance.quantity > product.quantity:
#         raise Exception("Out of Stock")


