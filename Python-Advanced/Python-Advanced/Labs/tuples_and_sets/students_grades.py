n = int(input())
student_grades = {}

for _ in range(n):
    student, grade = input().split()
    grade = float(grade)
    if student not in student_grades:
        student_grades[student] = []
    student_grades[student].append(grade)

for data in student_grades.items():
    print(f"{data[0]} -> {' '.join([f'{el:.2f}' for el in data[1]])} "
          f"(avg: {sum(data[1]) / len(data[1]):.2f})")
