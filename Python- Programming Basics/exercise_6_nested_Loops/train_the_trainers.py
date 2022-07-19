num_jury = int(input())
name_presentation = input()
curr_presentation_grades = 0
total_grades = 0
grade_cnt = 0
current_grade_cnt = 0
while name_presentation != 'Finish':
    for n in range(num_jury):
        grade = float(input())
        grade_cnt += 1
        current_grade_cnt += 1
        curr_presentation_grades += grade
        total_grades += grade
        average_score = curr_presentation_grades / current_grade_cnt
        if current_grade_cnt == num_jury:
            print(f"{name_presentation} - {average_score:.2f}.")
            curr_presentation_grades = 0
            current_grade_cnt = 0
            name_presentation = input()
average_score_all = total_grades / grade_cnt
print(f"Student's final assessment is {average_score_all:.2f}.")


