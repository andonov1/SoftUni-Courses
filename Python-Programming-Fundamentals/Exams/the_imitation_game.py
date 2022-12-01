encrypted_message = input()

while True:
    command = input().split('|')
    if command[0] == "Decode":
        print(f"The decrypted message is: {''.join(encrypted_message)}")
        break
    elif command[0] == "Move":
        n = int(command[1])
        encrypted_message = encrypted_message[n:] + encrypted_message[:n]
    elif command[0] == "Insert":
        inx = int(command[1])
        value = command[2]
        encrypted_message = encrypted_message[:inx] + value + encrypted_message[inx:]
    else:
        substring = command[1]
        replacement = command[2]
        encrypted_message = encrypted_message.replace(substring, replacement)

