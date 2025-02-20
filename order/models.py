import random
import string
from django.db import models

from utils.models import CreateUpdateTracker


class Order(CreateUpdateTracker):
    market = models.ForeignKey(
        "market.Market", on_delete=models.PROTECT, related_name="orders"
    )
    order_id = models.CharField(max_length=255, unique=True)
    total_price = models.DecimalField(max_digits=20, decimal_places=9, default=0)
    
    @classmethod
    def generate_unique_code(cls):
        while True:
            letters = ''.join(random.choices(string.ascii_uppercase, k=2))
            digits = ''.join(random.choices(string.digits, k=5))
            order_id = f"{letters}{digits}"
            if not cls.objects.filter(order_id=order_id).exists():
                return order_id

    def save(self, *args, **kwargs):
        if not self.order_id:
            self.order_id = self.generate_unique_code()
        super().save(*args, **kwargs)

class OrderProduct(CreateUpdateTracker):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name="products")
    product = models.ForeignKey(
        "product.Product", on_delete=models.PROTECT, related_name="order_products"
    )
    stock = models.ForeignKey(
        "stock.Stock", on_delete=models.PROTECT, related_name="order_products"
    )
    quantity = models.PositiveIntegerField(default=0)
     
    price = models.DecimalField(max_digits=20, decimal_places=9, default=0)
    cost_price = models.DecimalField(max_digits=20, decimal_places=9, default=0)
    total_price = models.DecimalField(max_digits=20, decimal_places=9, default=0)
