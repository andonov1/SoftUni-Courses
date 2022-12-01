raw_key = input()

while True:
    command = input().split('>>>')
    if command[0] == "Generate":
        break
    elif command[0] == "Contains":
        substring = command[1]
        if substring in raw_key:
            print(f"{raw_key} contains {substring}")
        else:
            print("Substring not found!")
    elif command[0] == "Flip":
        state = command[1]
        start_inx = int(command[2])
        end_inx = int(command[3])
        first_half = raw_key[:start_inx]
        change = raw_key[start_inx:end_inx]
        second_half = raw_key[end_inx:]
        if state == "Upper":
            change = change.upper()
        else:
            change = change.lower()
        raw_key = first_half + change + second_half
        print(raw_key)
    else:
        start_inx = int(command[1])
        end_inx = int(command[2])
        first_half = raw_key[:start_inx]
        change = raw_key[start_inx:end_inx]
        second_half = raw_key[end_inx:]
        raw_key = first_half + second_half
        print(raw_key)

print(f"Your activation key is: {raw_key}")