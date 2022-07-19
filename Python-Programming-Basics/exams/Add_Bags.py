import math
from math import floor
price_luggage_20kg = float(input())
luggage_kg = float(input())
days_until_trip = int(input())
luggage_quantity = int(input())
price_per_luggage = 0
added_tax = 0
if luggage_kg < 10:
    price_per_luggage = price_luggage_20kg * 0.20
elif luggage_kg <= 20:
    price_per_luggage = price_luggage_20kg * 0.50
else:
    price_per_luggage = price_luggage_20kg
if days_until_trip > 30:
    added_tax = 0.10
elif days_until_trip >= 7:
    added_tax = 0.15
else:
    added_tax = 0.40
price_per_luggage = price_per_luggage + (price_per_luggage * added_tax)
total_price = luggage_quantity * price_per_luggage
print(f" The total price of bags is: {total_price:.2f} lv. ")