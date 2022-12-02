stops = input()

while True:
    command = input().split(':')
    if command[0] == 'Travel':
        break
    elif command[0] == 'Add Stop':
        inx = int(command[1])
        stop = command[2]
        if 0 <= inx < len(stops):
            first_part = stops[:inx]
            second_part = stops[inx:]
            stops = first_part + stop + second_part
        print(stops)
    elif command[0] == 'Remove Stop':
        start_inx = int(command[1])
        end_inx = int(command[2])
        if 0 <= start_inx < len(stops) and 0 <= end_inx < len(stops):
            first_part = stops[:start_inx]
            second_part = stops[end_inx + 1:]
            stops = first_part + second_part
        print(stops)

    else:
        old_string = command[1]
        new_string = command[2]
        cnt = stops.count(old_string)
        if cnt:
            for i in range(cnt):
                start_inx = stops.find(old_string)
                end_inx = start_inx + len(old_string)
                first_part = stops[:start_inx]
                second_part = stops[end_inx:]
                stops = first_part + new_string + second_part
        print(stops)
print(f"Ready for world tour! Planned stops: {stops}")
