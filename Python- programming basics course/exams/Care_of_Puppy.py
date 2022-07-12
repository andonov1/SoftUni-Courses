total_food_kg = int(input())
command = input()
total_food_gr = total_food_kg * 1000

while command != 'Adopted':
    grams_eaten = int(command)
    total_food_gr -= grams_eaten
    command = input()
needed_food = abs(total_food_gr)
if command == 'Adopted':
    if total_food_gr >= 0:
        print(f"Food is enough! Leftovers: {total_food_gr} grams.")
    else:
        print(f"Food is not enough. You need {needed_food} grams more.")