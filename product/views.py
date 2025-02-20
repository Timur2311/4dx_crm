from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Product, StockProduct
from .serializers import ProductSerializer
from django.db.models import Prefetch, Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

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
            .select_related("group", "measurement", "market")
        )
        
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'market', openapi.IN_QUERY, description="Filter by market", type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                'group', openapi.IN_QUERY, description="Filter by group", type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                'search', openapi.IN_QUERY, description="Search by name or code", type=openapi.TYPE_STRING
            ),
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
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
        
    def get_object(self):
        return self.get_queryset().get(pk=self.kwargs['pk'])