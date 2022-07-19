type_flower = input()
quantity_flowers = int(input())
budget = int(input())

discount_increase = 0
discount_decrease = 0
flower_price = 0
if type_flower == 'Roses':
    flower_price = 5
    if quantity_flowers > 80:
        discount_decrease = 0.1
elif type_flower == 'Dahlias':
    flower_price = 3.80
    if quantity_flowers > 90:
        discount_decrease = 0.15
elif type_flower == 'Tulips':
    flower_price = 2.80
    if quantity_flowers > 80:
        discount_decrease = 0.15
elif type_flower == 'Narcissus':
    flower_price = 3
    if quantity_flowers < 120:
        discount_increase = 0.15
elif type_flower == 'Gladiolus':
    flower_price = 2.50
    if quantity_flowers < 80:
        discount_increase = 0.20

total_price = flower_price * quantity_flowers
total_price -= total_price * discount_decrease
total_price += total_price * discount_increase
diff = abs(total_price - budget)
if budget >= total_price:
    print(f'Hey, you have a great garden with {quantity_flowers} {type_flower} and {diff:.2f} leva left.')
else:
    print(f'Not enough money, you need {diff:.2f} leva more.')