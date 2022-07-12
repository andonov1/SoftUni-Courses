people = int(input())
season = input()
price = 0
if people <= 5:
    if season == 'spring':
        price = 50
    elif season == 'summer':
        price = 48.50
        price -= price * 0.15
    elif season == 'autumn':
        price = 60
    elif season == 'winter':
        price = 86
        price += price * 0.08
if people > 5:
    if season == 'spring':
        price = 48
    elif season == 'summer':
        price = 45
        price -= price * 0.15
    elif season == 'autumn':
        price = 49.50
    elif season == 'winter':
        price = 85
        price += price * 0.08
total_price = people * price
print(f'{total_price:.2f} leva.')
