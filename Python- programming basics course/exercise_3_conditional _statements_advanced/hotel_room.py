month = input()
number_days = int(input())

studio_price = 0
apartment_price = 0
discount = 0
if month == 'May' or month == 'October':
    studio_price = 50
    apartment_price = 65
elif month == 'June' or month == 'September':
    studio_price = 75.20
    apartment_price = 68.70
elif month == 'July' or month == 'August':
    studio_price = 76
    apartment_price = 77

if month == 'May' or month == 'October':
    if number_days > 14:
        studio_price = studio_price * 0.70
    elif number_days > 7:
        studio_price = studio_price * 0.95
elif month == 'June' or month == 'September':
    if number_days > 14:
        studio_price = studio_price * 0.80
if number_days > 14:
    apartment_price = apartment_price * 0.90

apartment_total = apartment_price * number_days
studio_total = studio_price * number_days
print(f'Apartment: {apartment_total:.2f} lv.')
print(f'Studio: {studio_total:.2f} lv.')
