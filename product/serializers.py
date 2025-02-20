from rest_framework import serializers

from product import models as product_models
from stock import serializers as stock_serializers
from market.serializers import MarketSerializer

class ProductGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = product_models.ProductGroup
        fields = ("id", "name")
        


class StockProductSerializer(serializers.ModelSerializer):
    stock = stock_serializers.StockSerializer(read_only=True)

    class Meta:
        model = product_models.StockProduct
        fields = ["stock", "quantity"]


class ProductSerializer(serializers.ModelSerializer):
    group = ProductGroupSerializer(read_only=True)
    market = MarketSerializer(read_only=True)
    measurement = serializers.SlugRelatedField(slug_field="name", read_only=True)
    stock_products = StockProductSerializer(many=True)
    total_balance = serializers.SerializerMethodField()

    class Meta:
        model = product_models.Product
        fields = (
            "id",
            "name",
            "market",
            "code",
            "group",
            "measurement",
            "total_balance",
            "stock_products",
        )

    def get_total_balance(self, obj):
        return getattr(obj, "total_balance", 0)
