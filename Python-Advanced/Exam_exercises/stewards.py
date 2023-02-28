from collections import deque

rotations = 0
seat_matches = 0
matched_seats = []

seats = input().split(', ')
first_seq = deque([s for s in input().split(', ')])
second_seq = deque([s for s in input().split(', ')])

while rotations < 10 and seat_matches < 3:
    rotations += 1
    first_num = first_seq.popleft()
    second_num = second_seq.pop()
    ascii_value = chr(int(first_num) + int(second_num))

    if first_num + ascii_value in seats:
        if first_num + ascii_value not in matched_seats:
            seat_matches += 1
            matched_seats.append(first_num + ascii_value)
        else:
            continue
    elif second_num + ascii_value in seats:
        if second_num + ascii_value not in matched_seats:
            seat_matches += 1
            matched_seats.append(second_num + ascii_value)
        else:
            continue

    else:
        first_seq.append(first_num)
        second_seq.appendleft(second_num)

print(f'Seat matches: {", ".join(s for s in matched_seats)}')
print(f'Rotations count: {rotations}')