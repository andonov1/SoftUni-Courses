budget = float(input())
statists = int(input())
price_clothing_per_statist = float(input())

decor = budget * 0.10
if statists > 150:
    price_clothing_per_statist = price_clothing_per_statist * 0.90
clothing_total = statists * price_clothing_per_statist
if (decor + clothing_total) > budget:
    print('Not enough money!')
    print(f'Wingard needs {abs(budget - (clothing_total + decor)):.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {abs(budget - (clothing_total + decor)):.2f} leva left.')
