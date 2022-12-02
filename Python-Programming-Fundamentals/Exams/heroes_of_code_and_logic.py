n = int(input())
heroes = {}

for i in range(n):
    data = input().split()
    hero = data[0]
    hp = int(data[1])
    mp = int(data[2])
    heroes[hero] = [hp, mp]

while True:
    command = input().split(' - ')
    if command[0] == 'End':
        break
    elif command[0] == 'CastSpell':
        hero = command[1]
        mp_needed = int(command[2])
        spell_name = command[3]
        if heroes[hero][1] >= mp_needed:
            heroes[hero][1] -= mp_needed
            print(f"{hero} has successfully cast {spell_name} and now has {heroes[hero][1]} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")
    elif command[0] == "TakeDamage":
        hero = command[1]
        damage = int(command[2])
        attacker = command[3]
        heroes[hero][0] -= damage
        if heroes[hero][0] > 0:
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes[hero][0]} HP left!")
        else:
            print(f"{hero} has been killed by {attacker}!")
            heroes.pop(hero)
    elif command[0] == "Recharge":
        hero = command[1]
        amount = int(command[2])
        temp = heroes[hero][1]
        heroes[hero][1] += amount
        if heroes[hero][1] > 200:
            heroes[hero][1] = 200
            print(f"{hero} recharged for {200 - temp} MP!")

        else:
            print(f"{hero} recharged for {amount} MP!")
    else:
        hero = command[1]
        amount = int(command[2])
        temp = heroes[hero][0]
        heroes[hero][0] += amount
        if heroes[hero][0] > 100:
            heroes[hero][0] = 100
            print(f"{hero} healed for {100 - temp} HP!")

        else:
            print(f"{hero} healed for {amount} HP!")

for key, value in heroes.items():
    print(f"{key}\n  HP: {value[0]}\n  MP: {value[1]}")
