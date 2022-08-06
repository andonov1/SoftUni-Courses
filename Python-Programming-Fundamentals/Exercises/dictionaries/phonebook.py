command = input()
phonebook = {}
while "-" in command:
    name, phone = command.split('-')
    phonebook[name] = phone
    command = input()

for i in range(int(command)):
    searched_name = input()
    if searched_name in phonebook:
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")
