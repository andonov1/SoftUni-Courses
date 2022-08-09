num_rooms = int(input())
total_free_chairs = 0
for number_of_room in range(1, num_rooms + 1):
    current_chairs, current_visitors = input().split()
    total_free_chairs += len(current_chairs)
    if int(current_visitors) > len(current_chairs):
        needed_chairs_in_room = int(current_visitors) - len(current_chairs)
        print(f"{needed_chairs_in_room} more chairs needed in room {number_of_room}")
        total_free_chairs -= int(current_visitors)
    else:
        total_free_chairs -= int(current_visitors)

if total_free_chairs >= 0:
    print(f"Game On, {total_free_chairs} free chairs left")