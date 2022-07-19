hour_exam = int(input())
minute_exam = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

total_exam_minutes = hour_exam * 60 + minute_exam
total_arrival_minutes = arrival_hour * 60 + arrival_minute
diff = abs(total_exam_minutes - total_arrival_minutes)
if total_arrival_minutes > total_exam_minutes:
    print('Late')
    if diff >= 60:
        hours_late = diff // 60
        minutes_late = diff % 60
        print(f"{hours_late}:{minutes_late:02d} hours after the start")
    else:
        print(f'{diff} minutes after the start')
elif total_arrival_minutes <= total_exam_minutes and diff <= 30:
    hours_late = diff // 60
    minutes_late = diff % 60
    print('On time')
    if diff > 0:
        print(f'{minutes_late} minutes before the start')
else:
    print('Early')
    if diff >= 60:
        hours_early = diff // 60
        minutes_early = diff % 60
        print(f"{hours_early}:{minutes_early:02d} hours before the start")
    else:
        print(f'{diff} minutes before the start')

