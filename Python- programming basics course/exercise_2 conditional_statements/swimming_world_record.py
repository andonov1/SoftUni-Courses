import math
record_seconds = float(input())
distance_meters = float(input())
time_seconds_1_meter = float(input())

water_resistance_time = math.floor(distance_meters / 15) * 12.5
time_for_record_distance = distance_meters * time_seconds_1_meter
if (time_for_record_distance + water_resistance_time) < record_seconds:
    print(f'Yes, he succeeded! The new world record is {(time_for_record_distance + water_resistance_time):.2f} seconds.')
    print()
else:
    print(f'No, he failed! He was {abs(record_seconds - ( time_for_record_distance + water_resistance_time)):.2f} seconds slower.')


