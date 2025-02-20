from rest_framework import serializers
from order import models as order_models
from product import models as product_models
from market import models as market_models
from stock import models as stock_models
from django.db.models import Sum


class CreateProductsSerializer(serializers.Serializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=product_models.Product.objects.only("id"),
        required=True,
        write_only=True,
    )
    stock = serializers.PrimaryKeyRelatedField(
        queryset=stock_models.Stock.objects.only("id"), required=True, write_only=True
    )
    quantity = serializers.IntegerField(min_value=1, required=True, write_only=True)
    price = serializers.DecimalField(max_digits=20, decimal_places=9, write_only=True)
    cost_price = serializers.DecimalField(
        max_digits=20,
        decimal_places=9,
        write_only=True,
        allow_null=True,
        required=False,
    )
    total_price = serializers.DecimalField(
        max_digits=20,
        decimal_places=9,
        write_only=True,
        required=False,
        allow_null=True,
    )

    def validate(self, data):
        product = data.get("product")
        stock = data.get("stock")
        quantity = data.get("quantity")

        not_enough_errors = []
        if not product_models.StockProduct.objects.filter(
            stock=stock, product=product, quantity__gte=quantity
        ).exists():
            not_enough_errors.append(f"{product.name} in {stock.name}")

        if not_enough_errors:
            errors = ", ".join(not_enough_errors)
            raise serializers.ValidationError(f"There is not enough products: {errors}")

        return super().validate(data)


class CreateOrderSerializer(serializers.Serializer):
    market = serializers.PrimaryKeyRelatedField(
        queryset=market_models.Market.objects.all(), required=True, write_only=True
    )
    products = CreateProductsSerializer(many=True, required=True, write_only=True)

    def create(self, validated_data):
        market = validated_data.pop("market")
        products = validated_data.get("products")
        order = order_models.Order.objects.create(market=market)
        order_products = [
            order_models.OrderProduct(
                order=order,
                product=product["product"],
                stock=product["stock"],
                quantity=product["quantity"],
                price=product["price"],
                cost_price=product["cost_price"],
                total_price=product["price"] * product["quantity"],
            )
            for product in products
        ]
        order_models.OrderProduct.objects.bulk_create(order_products)
        order.total_price = (
            order.products.aggregate(total=Sum("total_price"))["total"] or 0
        )
        order.save()
        return order

    def to_representation(self, instance):
        return {"order_id": instance.order_id}
