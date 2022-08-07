people_waiting = int(input())
wagons = [int(x) for x in input().split()]
lift_full = False
no_more_people = False

for i in range(len(wagons)):
    if i == len(wagons) - 1 and wagons[i] == 4:
        lift_full = True
    while wagons[i] < 4:
        wagons[i] += 1
        people_waiting -= 1
        if i == len(wagons) - 1 and wagons[i] == 4:
            lift_full = True
        if people_waiting < 1:
            no_more_people = True
        if no_more_people or lift_full:
            break
    if no_more_people or lift_full:
        break
wagons = [str(x) for x in wagons]
if no_more_people and not lift_full:
    print(f"The lift has empty spots!\n"
          f"{' '.join(wagons)}")

if lift_full and not no_more_people:
    print(f"There isn't enough space! {people_waiting} people in a queue!\n"
          f"{' '.join(wagons)}")

if lift_full and no_more_people:
    print(' '.join(wagons))
