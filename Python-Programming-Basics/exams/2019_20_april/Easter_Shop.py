eggs_in_shop = int(input())
command = input()
eggs_sold = 0
while command != 'Close':
    current_num = int(input())
    if command == 'Buy':
        if eggs_in_shop >= current_num:
            eggs_sold += current_num
            eggs_in_shop -= current_num
        else:
            print("Not enough eggs in store!")
            print(f"You can buy only {eggs_in_shop}.")
            break
    if command == 'Fill':
        eggs_in_shop += current_num
    command = input()
if command == 'Close':
    print("Store is closed!")
    print(f"{eggs_sold} eggs sold.")



