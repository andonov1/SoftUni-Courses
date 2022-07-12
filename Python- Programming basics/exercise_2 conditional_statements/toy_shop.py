trip_price = float(input())
puzzle_quantity = int(input())
doll_quantity = int(input())
bear_quantity = int(input())
minion_quantity = int(input())
truck_quantity = int(input())

total_quantity = puzzle_quantity + doll_quantity + bear_quantity + minion_quantity + truck_quantity
total_price = puzzle_quantity * 2.60 + doll_quantity * 3 + bear_quantity * 4.10 + minion_quantity * 8.20 + truck_quantity * 2
if total_quantity >= 50:
    total_price = total_price * 0.75
total_price = total_price * 0.90
if total_price >= trip_price:
    print(f'Yes! {total_price - trip_price:.2f} lv left.')
else:
    print(f'Not enough money! {abs(total_price - trip_price):.2f} lv needed.')


