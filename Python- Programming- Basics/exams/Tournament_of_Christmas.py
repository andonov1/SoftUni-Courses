days = int(input())

win_total = 0
lose_total = 0
sum_total = 0

for i in range(days):
    sport = input()
    win = 0
    lose = 0
    sum = 0
    while True:
        if sport == "Finish":
            if win > lose:
                sum_total += sum * 1.1
                win_total += win
            else:
                sum_total += sum
                lose_total += lose
            break

        if sport == "win":
            sum += 20
            win += 1
        elif sport == "lose":
            lose += 1

        sport = input()

if win_total > lose_total:
    print(f"You won the tournament! Total raised money: {sum_total * 1.2:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {sum_total:.2f}")