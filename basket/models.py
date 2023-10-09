from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class BasketItem(models.Model):
    product = models.ForeignKey('store.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    def subtotal(self):
        return self.product.price * self.quantity
