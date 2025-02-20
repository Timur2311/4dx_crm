import random
import string
from django.db import models

from utils.models import CreateUpdateTracker


class Measurement(CreateUpdateTracker):
    name = models.CharField(max_length=255)


class ProductGroup(models.Model):
    name = models.CharField(max_length=255)


class Product(CreateUpdateTracker):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, unique=True)
    group = models.ForeignKey(
        ProductGroup, on_delete=models.PROTECT, related_name="products"
    )
    measurement = models.ForeignKey(
        Measurement, on_delete=models.PROTECT, related_name="measurements"
    )
    market = models.ForeignKey(
        "market.Market", on_delete=models.PROTECT, related_name="stock_products"
    )
    
    @classmethod
    def generate_unique_code(cls):
        while True:
            letters = ''.join(random.choices(string.ascii_uppercase, k=2))
            digits = ''.join(random.choices(string.digits, k=5))
            code = f"{letters}{digits}"
            if not cls.objects.filter(code=code).exists():
                return code

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = self.generate_unique_code()
        super().save(*args, **kwargs)


class StockProduct(CreateUpdateTracker):
    stock = models.ForeignKey(
        "stock.Stock", on_delete=models.PROTECT, related_name="stock_products"
    )
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="stock_products"
    )
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ("product", "stock")

    def __str__(self):
        return f"{self.product.name} in {self.stock.name}: {self.quantity}"
