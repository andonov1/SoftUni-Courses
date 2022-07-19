budget = float(input())
video_card = int(input())
processor = int(input())
ram = int(input())

total_video_card = video_card * 250
total_processor = (total_video_card * 0.35) * processor
total_ram = ram * (total_video_card * 0.10)
total_cost = total_video_card + total_processor + total_ram
if video_card > processor:
    total_cost = total_cost * 0.85
if budget >= total_cost:
    print(f'You have {budget - total_cost:.2f} leva left!')
else:
    print(f'Not enough money! You need {abs(budget - total_cost):.2f} leva more!')


