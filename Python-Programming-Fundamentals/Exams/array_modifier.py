given_arr = [int(s) for s in input().split()]

while True:
    command = input().split()
    if command[0] == "end":
        break
    elif command[0] == "swap":
        inx_1 = int(command[1])
        inx_2 = int(command[2])
        given_arr[inx_1], given_arr[inx_2] = given_arr[inx_2], given_arr[inx_1]
    elif command[0] == "multiply":
        inx_1 = int(command[1])
        inx_2 = int(command[2])
        given_arr[inx_1] = given_arr[inx_1] * given_arr[inx_2]
    else:
        given_arr = [x - 1 for x in given_arr]

print(', '.join(str(x) for x in given_arr))

