
from django.urls import path
from .views import ProductListView, ProductDetailAPIView
urlpatterns = [
    path('', ProductListView.as_view(), name = 'products'),
    path('<int:pk>/', ProductDetailAPIView.as_view(), name = 'product_detail'),
]
