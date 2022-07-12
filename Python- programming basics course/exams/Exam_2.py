price_party = float(input())
quantity_love_messages = int(input())
quantity_roses = int(input())
quantity_keychain = int(input())
quantity_pictures = int(input())
quantity_surprises = int(input())

total_quantity = quantity_love_messages + quantity_roses + quantity_keychain + quantity_pictures + quantity_surprises
messages = quantity_love_messages * 0.60
roses = quantity_roses * 7.20
keychain = quantity_keychain * 3.60
pictures = quantity_pictures * 18.20
surprises = quantity_surprises * 22
total_cost = messages + roses + keychain + pictures + surprises
if total_quantity >= 25:
    total_cost -= total_cost * 0.35
total_cost -= total_cost * 0.10
left_money = abs(total_cost - price_party)
if total_cost >= price_party:
    print(f"Yes! {left_money:.2f} lv left.")
else:
    print(f"Not enough money! {left_money:.2f} lv needed.")