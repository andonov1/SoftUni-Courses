num_orders = int(input())
total_price = 0
for i in range(num_orders):
    capsule_price = float(input())
    days = int(input())
    capsules_needed = int(input())
    if 0.01 <= capsule_price <= 100 and 1 <= days <= 31 and 1 <= capsules_needed <= 2000:
        price = capsule_price * capsules_needed * days
        total_price += price
        print(f"The price for the coffee is: ${price:.2f}")
    else:
        continue

print(f"Total: ${total_price:.2f}")