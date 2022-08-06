stocks = {}
command = input()
while command != 'buy':
    name, price, quantity = command.split()
    if name not in stocks:
        stocks[name] = [0, 0]
        stocks[name][0] = float(price)
        stocks[name][1] = int(quantity)
    else:
        stocks[name][0] = float(price)
        stocks[name][1] += int(quantity)
    command = input()

for key, value in stocks.items():
    print(f'{key} -> {stocks[key][0] * stocks[key][1]:.2f}')