minutes_walk = int(input())
walks_per_day = int(input())
calories = float(input())

total_minutes_day = minutes_walk * walks_per_day
calories_burn = 5 * total_minutes_day
required_calories = calories * 0.5
if calories_burn >= required_calories:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_burn}.")
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {calories_burn}.')