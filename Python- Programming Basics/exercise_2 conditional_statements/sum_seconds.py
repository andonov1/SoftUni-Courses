first_time = int(input())
second_time = int(input())
third_time = int(input())

total_time_seconds = first_time + second_time + third_time
total_minutes = total_time_seconds // 60
total_seconds = total_time_seconds % 60
if total_seconds >= 10:
    print(f'{total_minutes}:{total_seconds}')
else:
    print(f'{total_minutes}:0{total_seconds}')


