lilly_age = int(input())
price_washer = float(input())
price_toys = int(input())
toys_cnt = 0
total_money = 0

for current_age in range(1, lilly_age + 1):
    if current_age % 2 != 0:
        toys_cnt += 1
    else:
        money_given = (5 * current_age) - 1
        total_money += money_given
total_toys_sold = toys_cnt * price_toys
total_money += total_toys_sold
money_left = abs(total_money - price_washer)
if total_money >= price_washer:
    print(f'Yes! {money_left:.2f}')
else:
    print(f'No! {money_left:.2f}')