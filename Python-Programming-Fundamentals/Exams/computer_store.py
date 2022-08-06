command = input()
type_customers = ['special', 'regular']
total_price = 0
price_with_taxes = 0
while command not in type_customers:
    price = float(command)
    if price < 0:
        print("Invalid price!")
    else:
        total_price += price
    command = input()
tax = total_price * 0.2
if command == 'regular':
    price_with_taxes += total_price + tax
if command == 'special':
    price_with_taxes += (total_price + tax) * 0.9
if total_price <= 0:
    print('Invalid order!')
else:
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {total_price:.2f}$\n"
          f"Taxes: {tax:.2f}$\n"
          "-----------\n"
          f"Total price: {price_with_taxes:.2f}$")
