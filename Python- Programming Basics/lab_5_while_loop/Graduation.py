name = input()
years_cnt = 0
cnt_fail_exams = 0
total_score = 0
while True:
    grade = float(input())
    years_cnt += 1
    if grade < 4:
        cnt_fail_exams += 1
        if cnt_fail_exams == 2:
            print(f"{name} has been excluded at {years_cnt} grade")
            break
        years_cnt -= 1
    else:
        total_score += grade
    if years_cnt == 12:
        average_grade = total_score / years_cnt
        print(f"{name} graduated. Average grade: {average_grade:.2f}")
        break