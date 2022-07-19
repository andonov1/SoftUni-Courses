name_player = input()
pts = 301
shots_cnt = 0
unsuccessful = 0
command = input()
while True:
    if command == 'Retire':
        print(f"{name_player} retired after {unsuccessful} unsuccessful shots.")
        break
    else:
        curr_pts = int(input())
    if command == 'Single':
        if curr_pts <= pts:
            shots_cnt += 1
    if command == 'Double':
        curr_pts += curr_pts
        if curr_pts <= pts:
            shots_cnt += 1
    if command == 'Triple':
        curr_pts += curr_pts * 2
        if curr_pts <= pts:
            shots_cnt += 1
    if curr_pts > pts:
        unsuccessful += 1
    else:
        pts -= curr_pts
    if pts == 0:
        print(f"{name_player} won the leg with {shots_cnt} shots.")
        break
    command = input()

