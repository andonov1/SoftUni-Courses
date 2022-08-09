quantity_food = float(input()) * 1000
quantity_hay = float(input()) * 1000
quantity_cover = float(input()) * 1000
pig_weight = float(input()) * 1000
must_go_to_shop = False
for i in range(1, 30 + 1):
    quantity_food -= 300
    if i % 2 == 0:
        quantity_hay -= quantity_food * 0.05
    if i % 3 == 0:
        quantity_cover -= pig_weight * 1/3
    if quantity_food / 1000 <= 0 or quantity_hay / 1000 <= 0 or quantity_cover / 1000 <= 0:
        print("Merry must go to the pet store!")
        must_go_to_shop = True
        break
if not must_go_to_shop:
    print(f"Everything is fine! Puppy is happy! Food: {quantity_food/1000:.2f}"
          f", Hay: {quantity_hay/1000:.2f}, Cover: {quantity_cover/1000:.2f}.")
