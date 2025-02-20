from rest_framework import serializers
from market import models as market_models


class MarketSerializer(serializers.ModelSerializer):

    class Meta:
        model = market_models.Market
        fields = ("id", "name")