pirate_ship = [int(s) for s in input().split('>')]
warship =[int(s) for s in input().split('>')]
maximum_health = int(input())
stalemate = True

while True:
    command = input().split()
    if command[0] == "Retire":
        break
    elif command[0] == "Fire":
        inx = int(command[1])
        damage = int(command[2])
        if 0 <= inx < len(warship):
            warship[inx] -= damage
            if warship[inx] <= 0:
                stalemate = False
                print("You won! The enemy ship has sunken.")
                break
    elif command[0] == "Defend":
        start_inx = int(command[1])
        end_inx = int(command[2])
        damage = int(command[3])
        if 0 <= start_inx < len(pirate_ship) and 0 <= end_inx < len(pirate_ship):
            for i in range(start_inx, end_inx + 1):
                pirate_ship[i] -= damage
                if pirate_ship[i] <= 0:
                    stalemate = False
                    print("You lost! The pirate ship has sunken.")
                    break
    elif command[0] == "Repair":
        inx = int(command[1])
        health = int(command[2])
        if 0 <= inx < len(pirate_ship):
            pirate_ship[inx] += health
            if pirate_ship[inx] > maximum_health:
                pirate_ship[inx] = maximum_health
    else:
        sections_to_repair = [x for x in pirate_ship if x < maximum_health * 0.2]
        print(f"{len(sections_to_repair)} sections need repair.")

if stalemate:
    print(f"Pirate ship status: {sum(pirate_ship)}"
          f"\nWarship status: {sum(warship)}")

