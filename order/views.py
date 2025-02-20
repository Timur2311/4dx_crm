from order.serializers import CreateOrderSerializer
from rest_framework.generics import CreateAPIView
from order.models import Order
from rest_framework.response import Response

class CreateOrderAPIView(CreateAPIView):
    serializer_class = CreateOrderSerializer
    queryset = Order.objects.all()
    
