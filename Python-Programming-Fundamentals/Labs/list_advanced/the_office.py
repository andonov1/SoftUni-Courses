num = [int(i) for i in input().split()]
factor = int(input())

happiness = [el*factor for el in num]
threshold = sum(happiness) / len(happiness)

happy_employees = [i for i in happiness if i >= threshold]
sad_employees = [i for i in happiness if i < threshold]

if len(happy_employees) >= len(happiness) / 2:
    print(f'Score: {len(happy_employees)}/{len(happiness)}. Employees are happy!')
else:
    print(f'Score: {len(happy_employees)}/{len(happiness)}. Employees are not happy!')