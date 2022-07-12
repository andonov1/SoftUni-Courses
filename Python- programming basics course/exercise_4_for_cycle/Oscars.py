name_actor = input()
points = float(input())
number_judges = int(input())
total_points = points

for i in range(number_judges):
    name_judge = input()
    judge_points = float(input())
    total_points += len(name_judge) * (judge_points / 2)
    if total_points > 1250.5:
        print(f'Congratulations, {name_actor} got a nominee for leading role with {total_points:.1f}!')
        break
diff = abs(1250.5 - total_points)
if total_points <= 1250.5:
    print(f'Sorry, {name_actor} you need {diff:.1f} more!')
