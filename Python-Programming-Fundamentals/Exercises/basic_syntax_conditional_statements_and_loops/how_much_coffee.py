command = input()
coffees_needed = 0
while command != "END":
    if command.lower() == 'coding' or command.lower() == "dog" or command.lower() == 'cat' or command.lower() == 'movie':
        if command.islower():
            coffees_needed += 1
        else:
            coffees_needed += 2
    command = input()

if coffees_needed > 5:
    print("You need extra sleep")
else:
    print(coffees_needed)
