trip_cost = float(input())
curr_balance = float(input())

spending_cnt = 0
days_cnt = 0
while curr_balance < trip_cost and spending_cnt < 5:
    command = input()
    money = float(input())
    days_cnt += 1
    if command == 'save':
        curr_balance += money
        spending_cnt = 0
    elif command == 'spend':
        curr_balance -= money
        spending_cnt += 1
        if curr_balance < 0:
            curr_balance = 0
if spending_cnt >= 5:
    print(f"You can't save the money.")
    print(days_cnt)
if curr_balance >= trip_cost:
    print(f"You saved the money for {days_cnt} days.")


