movie_name = input()
taken_seats = 0
curr_student = 0
curr_standard = 0
curr_kid = 0
total_taken_seats = 0
hall_full = False
while movie_name != 'Finish':
    hall_seats = int(input())
    type_seat = input()
    while type_seat != 'End':
        total_taken_seats += 1
        taken_seats += 1
        if type_seat == 'student':
            curr_student += 1
        elif type_seat == 'standard':
            curr_standard += 1
        else:
            curr_kid += 1
        if taken_seats >= hall_seats:
            hall_full = True
            break
        type_seat = input()
    if hall_full or type_seat == 'End':
        hall_full_percent = (taken_seats / hall_seats) * 100
        print(f"{movie_name} - {hall_full_percent:.2f}% full.")
        taken_seats = 0
        movie_name = input()

student_percent = (curr_student / total_taken_seats) * 100
standard_percent = (curr_standard / total_taken_seats) * 100
kids_percent = (curr_kid / total_taken_seats) * 100
print(f"Total tickets: {total_taken_seats}")
print(f"{student_percent:.2f}% student tickets.")
print(f"{standard_percent:.2f}% standard tickets.")
print(f"{kids_percent:.2f}% kids tickets.")






