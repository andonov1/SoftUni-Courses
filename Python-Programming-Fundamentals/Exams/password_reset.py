password = input()

while True:
    command = input().split()
    if command[0] == 'Done':
        break
    elif command[0] == 'TakeOdd':
        new_password = ''
        for i in range(len(password)):
            if i % 2 != 0:
                new_password += password[i]
        password = new_password
        print(password)
    elif command[0] == 'Cut':
        inx = int(command[1])
        length = int(command[2])
        first_part = password[:inx]
        second_part = password[inx + length:]
        password = first_part + second_part
        print(password)
    else:
        substring = command[1]
        substitute = command[2]
        cnt = password.count(substring)
        if cnt:
            for i in range(cnt):
                start_inx = password.find(substring)
                end_inx = start_inx + len(substring)
                first_part = password[:start_inx]
                second_part = password[end_inx:]
                password = first_part + substitute + second_part
            print(password)
        else:
            print("Nothing to replace!")

print(f"Your password is: {password}")