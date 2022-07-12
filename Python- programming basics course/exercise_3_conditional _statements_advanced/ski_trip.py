trip_days = int(input()) - 1
type_room = input()
rating = input()

room_for_one_person = 18
apartment = 25
president_apartment = 35

if trip_days < 10:
    apartment = apartment * 0.70
    president_apartment = president_apartment * 0.90
elif 10 <= trip_days <= 15:
    apartment = apartment * 0.65
    president_apartment = president_apartment * 0.85
else:
    apartment = apartment * 0.50
    president_apartment = president_apartment * 0.80

if type_room == 'apartment':
    total_cost = apartment * trip_days
    if rating == 'positive':
        total_cost = total_cost * 1.25
    else:
        total_cost = total_cost * 0.90
elif type_room == 'room for one person':
    total_cost = room_for_one_person * trip_days
    if rating == 'positive':
        total_cost = total_cost * 1.25
    else:
        total_cost = total_cost * 0.90
else:
    total_cost = president_apartment * trip_days
    if rating == 'positive':
        total_cost = total_cost * 1.25
    else:
        total_cost = total_cost * 0.90
print(f'{total_cost:.2f}')
