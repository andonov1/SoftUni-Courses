type_projection = input()
rows = int(input())
column = int(input())
total_income = 0
number_seats = rows * column
if type_projection == 'Premiere':
    total_income = number_seats * 12
elif type_projection == 'Normal':
    total_income = number_seats * 7.50
elif type_projection == 'Discount':
    total_income = number_seats * 5
print(f'{total_income:.2f} leva')
