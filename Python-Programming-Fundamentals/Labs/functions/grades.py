def grade_result(grade):
    if 2.00 <= grade <= 2.99:
        print('Fail')
    elif 3.00 <= grade <= 3.49:
        print('Poor')
    elif 3.50 <= grade <= 4.49:
        print('Good')
    elif 4.50 <= grade <= 5.49:
        print('Very Good')
    if 5.50 <= grade <= 6.00:
        print('Excellent')


grade_num = float(input())
grade_result(grade_num)
