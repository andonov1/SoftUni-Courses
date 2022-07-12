percent_fats = int(input()) / 100
percent_proteins = int(input()) / 100
percent_carbs = int(input()) / 100
total_calories = int(input())
percent_water = int(input())

total_fats = (total_calories * percent_fats) / 9
total_protein = (total_calories * percent_proteins) / 4
total_carbs = (total_calories * percent_carbs) / 4
total_food = total_fats + total_protein + total_carbs
calories_per_gram = total_calories / total_food
without_water_percent = (100 - percent_water) / 100
without_water = calories_per_gram * without_water_percent

print(f'{without_water:.4f}')