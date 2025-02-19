import os
import django
import random

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")  # Replace with your project name
django.setup()

from product.models import Measurement, ProductGroup, Product, StockProduct
from market.models import Market
from stock.models import Stock

# Create Measurements
measurements = ["kg", "liters", "pieces"]
measurement_objs = [Measurement.objects.create(name=m) for m in measurements]

# Create Product Groups
product_groups = ["Electronics", "Furniture", "Groceries"]
group_objs = [ProductGroup.objects.create(name=g) for g in product_groups]

# Create Markets
market_names = ["SuperMart", "MegaStore", "TechHub"]
market_objs = [Market.objects.create(name=m) for m in market_names]

# Create Stocks
stock_locations = ["Warehouse A", "Warehouse B", "Retail Store"]
stock_objs = [Stock.objects.create(name=s, market=market_objs[0]) for s in stock_locations]

# Create Products
products = []
for i in range(10):  # Creating 10 products
    product = Product.objects.create(
        name=f"Product {i+1}",
        code=f"P-{1000 + i}",
        group=random.choice(group_objs),
        measurement=random.choice(measurement_objs),
        market=random.choice(market_objs)
    )
    products.append(product)

# Create StockProducts (random quantities in random stocks)
for product in products:
    for stock in random.sample(stock_objs, random.randint(1, 3)):  # Assign each product to 1-3 stocks
        StockProduct.objects.create(
            stock=stock,
            product=product,
            quantity=random.randint(5, 100)
        )

print("✅ Test data successfully created!")
