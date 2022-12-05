animals = {}
areas = {}
hungry_animals_by_area = {}

while True:
    command = input().split(': ')
    if command[0] == "EndDay":
        break
    elif command[0] == "Add":
        data = command[1].split('-')
        animal_name = data[0]
        needed_food = int(data[1])
        area = data[2]
        if animal_name not in animals:
            animals[animal_name] = needed_food
        else:
            animals[animal_name] += needed_food
        if area not in areas:
            areas[area] = [animal_name]
        else:
            if animal_name not in areas[area]:
                areas[area].append(animal_name)
    else:
        data = command[1].split('-')
        animal_name = data[0]
        food = int(data[1])
        if animal_name in animals:
            animals[animal_name] -= food
            if animals[animal_name] <= 0:
                print(f"{animal_name} was successfully fed")
                animals.pop(animal_name)

for animal in animals:
    for key, value in areas.items():
        if animal in value:
            if key not in hungry_animals_by_area:
                hungry_animals_by_area[key] = [animal]
            else:
                hungry_animals_by_area[key].append(animal)

print("Animals:")
for key, value in animals.items():
    print(f" {key} -> {value}g")
print("Areas with hungry animals:")
for key, value in hungry_animals_by_area.items():
    print(f" {key}: {len(value)}")