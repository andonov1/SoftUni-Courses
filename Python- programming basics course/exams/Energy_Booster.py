fruit = input()
size = input()
quantity = int(input())
price = 0
if fruit == 'Watermelon':
    if size == 'small':
        price = 56
        num = 2
    elif size == 'big':
        price = 28.70
        num = 5
elif fruit == 'Mango':
    if size == 'small':
        price = 36.66
        num = 2
    elif size == 'big':
        price = 19.6
        num = 5
elif fruit == 'Pineapple':
    if size == 'small':
        num = 2
        price = 42.10
    elif size == 'big':
        num = 5
        price = 24.80
elif fruit == 'Raspberry':
    if size == 'small':
        num = 2
        price = 20
    elif size == 'big':
        num = 5
        price = 15.20
total_price = quantity * (price * num)
if 400 <= total_price <= 1000:
    total_price -= total_price * 0.15
elif total_price > 1000:
    total_price -= total_price * 0.50
print(f"{total_price:.2f} lv.")
