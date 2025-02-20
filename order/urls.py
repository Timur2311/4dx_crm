
from django.urls import path
from order.views import CreateOrderAPIView
urlpatterns = [
    path('order/', CreateOrderAPIView.as_view(), name = 'order')
]
