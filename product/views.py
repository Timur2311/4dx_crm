from rest_framework.generics import ListAPIView
from .models import Product, StockProduct
from .serializers import ProductSerializer
from django.db.models import Prefetch, Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class ProductListView(ListAPIView):
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['market', 'group']
    search_fields = ['name', 'code']
    
    def get_queryset(self):

        return (
            Product.objects.annotate(total_balance=Sum("stock_products__quantity"))
            .prefetch_related(
                Prefetch(
                    "stock_products",
                    queryset=StockProduct.objects.select_related("stock").all(),
                )
            )
            .select_related("group", "measurement")
        )
