lost_fight = int(input())

helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet = lost_fight // 2
sword = lost_fight // 3
shield = lost_fight // 6
armor = shield // 2
expenses = helmet * helmet_price +\
    sword * sword_price +\
    shield * shield_price +\
    armor * armor_price
print(f'Gladiator expenses: {expenses:.2f} aureus')