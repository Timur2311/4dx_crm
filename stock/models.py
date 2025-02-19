from django.db import models

from utils.models import CreateUpdateTracker


class Stock(CreateUpdateTracker):
    BASIC = "basic"

    STOCK_TYPES = [(BASIC, "Basic")]
    stock_type = models.CharField(max_length=20, choices=STOCK_TYPES, default=BASIC)
    name = models.CharField(max_length=255)
    market = models.ForeignKey(
        "market.Market", on_delete=models.PROTECT, related_name="stocks"
    )
