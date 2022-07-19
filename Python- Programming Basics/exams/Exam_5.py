starting_point = 5364
peak = 8848
days_cnt = 1

condition = input()
while condition != 'END':
    meters = int(input())
    if condition == 'Yes':
        days_cnt += 1
        if days_cnt > 5:
            print(f"Failed!")
            print(f"{starting_point}")
            break
    starting_point += meters
    if starting_point >= peak:
        print(f"Goal reached for {days_cnt} days!")
        break
    condition = input()

if condition == 'END':
    if starting_point >= peak:
        print(f"Goal reached for {days_cnt} days!")
    else:
        print(f"Failed!")
        print(f"{starting_point}")
