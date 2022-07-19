from math import floor
coins = 0
change = float(input())
changeToSt = change * 100
changeToSt = floor(changeToSt)
while changeToSt > 0:
    if changeToSt >= 200:
        changeToSt -= 200
        coins += 1
    elif changeToSt >= 100:
        changeToSt -= 100
        coins += 1
    elif changeToSt >= 50:
        changeToSt -= 50
        coins += 1
    elif changeToSt >= 20:
        changeToSt -= 20
        coins += 1
    elif changeToSt >= 10:
        changeToSt -= 10
        coins += 1
    elif changeToSt >= 5:
        changeToSt -= 5
        coins += 1
    elif changeToSt >= 2:
        changeToSt -= 2
        coins += 1
    elif changeToSt >= 1:
        changeToSt -= 1
        coins += 1
print(coins)