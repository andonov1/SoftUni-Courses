from collections import deque


def convert_str_to_time(str_time):
    hours, minutes, seconds = [int(s) for s in str_time.split(':')]
    return hours * 60 * 60 + minutes * 60 + seconds


def convert_seconds_to_str_time(seconds):
    hours = seconds // (60 * 60)
    seconds %= (60 * 60)
    minutes = seconds // 60
    seconds %= 60
    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'


robots_data = input().split(';')
process_time_by_robot = {}
busy_robot_until = {}

for robot_data in robots_data:
    name, process_time = robot_data.split('-')
    process_time_by_robot[name] = int(process_time)
    busy_robot_until[name] = -1

time = convert_str_to_time(input())
items = deque()

while True:
    line = input()
    if line == 'End':
        break
    items.append(line)

while items:
    time += 1
    item = items.popleft()

    for name, busy_until in process_time_by_robot.items():
        if time >= busy_until:
            busy_robot_until[name] = time + process_time_by_robot[name]
            print(f'{name} - {item} [{convert_seconds_to_str_time(time)}]')
            break
    else:
        items.append(item)
