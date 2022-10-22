initial_loot = input().split('|')

while True:
    command = input().split()
    if command[0] == "Yohoho!":
        break
    elif command[0] == "Loot":
        [initial_loot.insert(0, x) for x in command[1:] if x not in initial_loot]
    elif command[0] == "Drop":
        inx = int(command[1])
        if 0 <= inx < len(initial_loot):
            loot = initial_loot.pop(inx)
            initial_loot.append(loot)

    else:
        count = int(command[1])
        stolen_loot = []
        if len(initial_loot) < count:
            stolen_loot = initial_loot
            initial_loot = []
            print(', '.join(stolen_loot))
        else:
            for i in range(count):
                stolen_loot.append(initial_loot.pop())
            print(', '.join(reversed(stolen_loot)))

if initial_loot:
    average_gain = sum([len(x) for x in initial_loot]) / len(initial_loot)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
