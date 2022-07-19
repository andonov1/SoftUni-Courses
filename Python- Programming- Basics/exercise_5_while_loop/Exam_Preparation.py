low_grade_minimum = int(input())
current_exercise = input()
low_grade_cnt = 0
exercise_cnt = 0
total_grades = 0
last_problem = ''
while current_exercise != 'Enough':
    grade = int(input())
    exercise_cnt += 1
    total_grades += grade
    last_problem = current_exercise
    if grade <= 4:
        low_grade_cnt += 1
        if low_grade_cnt >= low_grade_minimum:
            print(f"You need a break, {low_grade_cnt} poor grades.")
            break

    current_exercise = input()
average_score = total_grades / exercise_cnt
if current_exercise == 'Enough':
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {exercise_cnt}")
    print(f"Last problem: {last_problem}")


