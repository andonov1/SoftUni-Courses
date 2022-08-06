command = input()
companies_dict = {}

while command != 'End':
    company, employee = command.split(' -> ')
    if company not in companies_dict:
        companies_dict[company] = [employee]
    else:
        if employee not in companies_dict[company]:
            companies_dict[company].append(employee)
    command = input()

for key, value in companies_dict.items():
    print(key)
    for id in companies_dict[key]:
        print(f'-- {id}')

