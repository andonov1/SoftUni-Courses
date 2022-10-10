first_employee_capability_per_h = int(input())
second_employee_capability_per_h = int(input())
third_employee_capability_per_h = int(input())
students_cnt = int(input())
total_capability_per_hour = first_employee_capability_per_h + second_employee_capability_per_h + \
                            third_employee_capability_per_h
hrs_cnt = 0
while students_cnt > 0:
    hrs_cnt += 1
    if hrs_cnt % 4 == 0:
        continue
    students_cnt -= total_capability_per_hour

print(f"Time needed: {hrs_cnt}h.")