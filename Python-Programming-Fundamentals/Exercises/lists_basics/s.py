items = input().split('|')
budget = int(input())
bought_items_prices = []
spend = 0
n = 0
for i in items:
    item = i.split('->')
    price = float(item[1])
    if budget >= price:
        if item[0] == 'Clothes':
            if price <= 50:
                budget -= price
                spend += price
                bought_items_prices.insert(n, price * 1.4)
        elif item[0] == 'Shoes':
            if price <= 35:
                budget -= price
                spend += price
                bought_items_prices.insert(n, price * 1.4)
        elif item[0] == 'Accessories':
            if price <= 20.50:
                budget -= price
                spend += price
                bought_items_prices.insert(n, price * 1.4)
        else:
            budget -= price
            spend += price
            bought_items_prices.insert(n, price * 1.4)
        n += 1
profit = (spend * 1.4) - spend
budget += profit + spend
for i in range(len(bought_items_prices)):
    if i < len(bought_items_prices) - 1:
        print(f'{bought_items_prices[i]:.2f} ', end='')
    else:
        print(f'{bought_items_prices[i]:.2f}', end='')
print(f"Profit: {profit:.2f}")
if budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
