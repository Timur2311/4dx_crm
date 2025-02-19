from django.db import models
from utils.models import CreateUpdateTracker


class Market(CreateUpdateTracker):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)


class MarketBranch(CreateUpdateTracker):
    name = models.CharField(max_length=255)
    market = models.ForeignKey(
        Market, on_delete=models.PROTECT, related_name="branches"
    )
