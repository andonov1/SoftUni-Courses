budget = float(input())
season = input()
destination = ''
percent_cost = 0
housing = ''
if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        housing = 'Camp'
        percent_cost = 0.30
    else:
        housing = 'Hotel'
        percent_cost = 0.70
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        housing = 'Camp'
        percent_cost = 0.40
    else:
        housing = 'Hotel'
        percent_cost = 0.80
elif budget > 1000:
    destination = 'Europe'
    housing = 'Hotel'
    percent_cost = 0.90
total_cost = budget * percent_cost
print(f'Somewhere in {destination}')
print(f'{housing} - {total_cost:.2f}')


