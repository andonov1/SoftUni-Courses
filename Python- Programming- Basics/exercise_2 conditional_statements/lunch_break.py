from math import ceil
name_of_series = input()
episode_duration = int(input())
break_duration = int(input())

time_lunch = break_duration * 1/8
time_rest = break_duration * 1/4
needed_time = episode_duration + time_lunch + time_rest
diff = abs(needed_time - break_duration)
if needed_time <= break_duration:
    print(f'You have enough time to watch {name_of_series} and left with '
          f'{ceil(diff)} minutes free time.')
else:
    print(f"You don't have enough time to watch {name_of_series}, "
          f"you need {ceil(diff)} more minutes.")