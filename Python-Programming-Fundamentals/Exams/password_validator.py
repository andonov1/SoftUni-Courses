password = input()

while True:
    command = input().split()
    if command[0] == "Complete":
        break
    elif command[0] == "Make":
        state = command[1]
        inx = int(command[2])
        char = password[inx]
        first_part = password[:inx]
        second_part = password[inx + 1:]
        if state == "Upper":
            password = first_part + char.upper() + second_part
        else:
            password = first_part + char.lower() + second_part
        print(password)
    elif command[0] == 'Insert':
        inx = int(command[1])
        char = command[2]
        if 0 <= inx < len(password):
            first_part = password[:inx]
            second_part = password[inx:]
            password = first_part + char + second_part
        print(password)
    elif command[0] == 'Replace':
        char = command[1]
        value = int(command[2])
        ascii_value = ord(char)
        value_sum = ascii_value + value
        new_symbol = chr(value_sum)
        cnt = password.count(char)
        if cnt:
            for i in range(cnt):
                start_inx = password.find(char)
                end_inx = start_inx + len(char)
                first_part = password[:start_inx]
                second_part = password[end_inx:]
                password = first_part + new_symbol + second_part
            print(password)
    elif command[0] == 'Validation':
        uppercase_letters = 0
        lowercase_letters = 0
        digits = 0
        if len(password) < 8:
            print("Password must be at least 8 characters long!")
        for char in password:
            if char.islower():
                lowercase_letters += 1
            if char.isupper():
                uppercase_letters += 1
            if char.isdigit():
                digits += 1
            if not char.isalnum():
                if char != '_':
                    print("Password must consist only of letters, digits and _!")

        if uppercase_letters < 1:
            print("Password must consist at least one uppercase letter!")
        if lowercase_letters < 1:
            print("Password must consist at least one lowercase letter!")
        if digits < 1:
            print("Password must consist at least one digit!")