budget = int(input())
season = input()
number_fisherman = int(input())
price = 0
discount = 0
if season == 'Spring':
    price = 3000
elif season == 'Summer':
    price = 4200
elif season == 'Autumn':
    price = 4200
elif season == 'Winter':
    price = 2600
if number_fisherman <= 6:
    discount = 0.1
elif 7 <= number_fisherman <= 11:
    discount = 0.15
else:
    discount = 0.25

total_cost = price - (price * discount)
if season != 'Autumn':
    if number_fisherman % 2 == 0:
        total_cost = total_cost - (total_cost * 0.05)
diff = abs(total_cost - budget)
if budget >= total_cost:
    print(f'Yes! You have {diff:.2f} leva left.')
else:
    print(f'Not enough money! You need {diff:.2f} leva.')
