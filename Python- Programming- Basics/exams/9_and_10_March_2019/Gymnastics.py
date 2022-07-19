country = input()
sport = input()
difficulty = 0
performance = 0
if country == 'Russia':
    if sport == 'ribbon':
        difficulty = 9.100
        performance = 9.400
    elif sport == 'hoop':
        difficulty = 9.300
        performance = 9.800
    elif sport == 'rope':
        difficulty = 9.600
        performance = 9.000
elif country == 'Bulgaria':
    if sport == 'ribbon':
        difficulty = 9.600
        performance = 9.400
    elif sport == 'hoop':
        difficulty = 9.550
        performance = 9.750
    elif sport == 'rope':
        difficulty = 9.500
        performance = 9.400
elif country == 'Italy':
    if sport == 'ribbon':
        difficulty = 9.200
        performance = 9.500
    elif sport == 'hoop':
        difficulty = 9.450
        performance = 9.350
    elif sport == 'rope':
        difficulty = 9.700
        performance = 9.150
rating = difficulty + performance
percent = (rating / 20) * 100
needed_percent = 100 - percent
print(f'The team of {country} get {rating:.3f} on {sport}.')
print(f'{needed_percent:.2f}%')