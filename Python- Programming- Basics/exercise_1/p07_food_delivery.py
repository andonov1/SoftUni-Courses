chicken_menu = int(input())
fish_menu = int(input())
vegetarian_menu = int(input())

price_chicken = (chicken_menu * 10.35)
fish_price = (fish_menu * 12.40)
vegetarian_price = (vegetarian_menu * 8.15)
desert = (price_chicken + fish_price + vegetarian_price) * 0.20
delivery = 2.50
total_price = price_chicken + fish_price + vegetarian_price + desert + delivery
print(total_price)