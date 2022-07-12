destination = input()
my_budget = 0
while destination != 'End':
    budget_required = float(input())
    while my_budget <= budget_required:
        current_sum = float(input())
        my_budget += current_sum
        if my_budget >= budget_required:
            print(f'Going to {destination}!')
            break
    my_budget = 0
    destination = input()



