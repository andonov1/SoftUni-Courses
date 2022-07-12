import sys

command = input()
most_goals = -sys.maxsize
player_most_goals = ''
while command != 'END':
    goals_scored = int(input())
    if goals_scored > most_goals:
        most_goals = goals_scored
        player_most_goals = command
        if most_goals >= 10:
            break
    name = input()

print(f"{player_most_goals} is the best player!")
if most_goals >= 3:
    print(f"He has scored {most_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {most_goals} goals.")
