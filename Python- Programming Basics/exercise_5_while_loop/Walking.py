curr_command = input()
steps_cnt = 0
while curr_command != 'Going home':
    steps = int(curr_command)
    steps_cnt += steps
    if steps_cnt >= 10000:
        break
    curr_command = input()
if curr_command == 'Going home':
    steps_going_home = int(input())
    steps_cnt += steps_going_home
steps_diff = abs(10000 - steps_cnt)
if steps_cnt >= 10000:
    print(f"Goal reached! Good job!")
    print(f"{steps_diff} steps over the goal!")
else:
    print(f"{steps_diff} more steps to reach goal.")