number_pages = int(input())
read_pages_hour = int(input())
days_needed = int(input())
total_time_hours = int(number_pages / read_pages_hour)
average_day_reading = total_time_hours / days_needed
print(average_day_reading)