import math

number_tournaments = int(input())
starting_points = int(input())
points = 0
wins = 0
for i in range(0, number_tournaments):
    result = input()
    if result == 'W':
        wins += 1
        points += 2000
    elif result == 'F':
        points += 1200
    elif result == 'SF':
        points += 720

final_points = starting_points + points
average_tournament_points = points / number_tournaments
percent_wins = (wins / number_tournaments) * 100

print(f'Final points: {final_points}')
print(f'Average points: {math.floor(average_tournament_points)}')
print(f'{percent_wins:.2f}%')

