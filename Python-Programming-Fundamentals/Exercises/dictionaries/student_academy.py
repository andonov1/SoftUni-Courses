n = int(input())
grades = {}

for _ in range(n):
    name = input()
    grade = float(input())
    if name not in grades:
        grades[name] = [grade]
    else:
        grades[name].append(grade)

for key, value in grades.items():
    result = sum(grades[key]) / len(grades[key])
    if result >= 4.50:
        print(f"{key} -> {result:.2f}")



