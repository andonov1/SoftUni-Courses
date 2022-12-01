concealed_message = input()
while True:
    command = input().split(":|:")
    if command[0] == "Reveal":
        break
    elif command[0] == "InsertSpace":
        inx = int(command[1])
        first_part = concealed_message[:inx]
        second_part = concealed_message[inx:]
        concealed_message = first_part + " " + second_part
        print(concealed_message)

    elif command[0] == 'Reverse':
        substring = command[1]
        if substring in concealed_message:
            start_inx = concealed_message.find(substring)
            end_inx = start_inx + len(substring)
            first_part = concealed_message[:start_inx]
            second_part = concealed_message[end_inx:]
            substring = substring[:: -1]
            concealed_message = first_part + second_part + substring
            print(concealed_message)
        else:
            print('error')
    else:
        substring = command[1]
        replacement = command[2]
        cnt = concealed_message.count(substring)
        if cnt:
            for i in range(cnt):
                start_inx = concealed_message.find(substring)
                end_inx = start_inx + len(substring)
                first_part = concealed_message[:start_inx]
                second_part = concealed_message[end_inx:]
                concealed_message = first_part + replacement + second_part
        print(concealed_message)
print(f"You have a new text message: {concealed_message}")
