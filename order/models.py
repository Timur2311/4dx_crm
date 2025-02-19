from django.db import models

from utils.models import CreateUpdateTracker


class Order(CreateUpdateTracker):
    market = models.ForeignKey(
        "market.Market", on_delete=models.PROTECT, related_name="orders"
    )
    total_price = models.DecimalField(max_digits=20, decimal_places=9, default=0)


class OrderProduct(CreateUpdateTracker):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name="products")
    product = models.ForeignKey(
        "product.Product", on_delete=models.PROTECT, related_name="order_products"
    )
    stock = models.ForeignKey(
        "stock.Stock", on_delete=models.PROTECT, related_name="order_products"
    )
    quantity = models.PositiveIntegerField(default=0)

    cost_price = models.DecimalField(max_digits=20, decimal_places=9, default=0)
    total_price = models.DecimalField(max_digits=20, decimal_places=9, default=0)
