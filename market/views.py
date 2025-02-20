from rest_framework.generics import ListAPIView
from market.models import Market
from market.serializers import MarketSerializer

class MarketListAPIView(ListAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer
