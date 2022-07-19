days = int(input())
total_food = float(input())
dog_eaten = 0
cat_eaten = 0
biscuit = 0
for i in range(1, days + 1):
    dog_food = float(input())
    cat_food = float(input())
    total_food_day = dog_food + cat_food
    if i % 3 == 0:
        biscuit += total_food_day * 0.1
    dog_eaten += dog_food
    cat_eaten += cat_food
percent_eaten_food = ((cat_eaten + dog_eaten) / total_food) * 100
percent_dog_eaten = (dog_eaten / (cat_eaten + dog_eaten)) * 100
percent_cat_eaten = (cat_eaten / (cat_eaten + dog_eaten)) * 100

print(f"Total eaten biscuits: {round(biscuit)}gr.")
print(f'{percent_eaten_food:.2f}% of the food has been eaten.')
print(f"{percent_dog_eaten:.2f}% eaten from the dog.")
print(f"{percent_cat_eaten:.2f}% eaten from the cat.")