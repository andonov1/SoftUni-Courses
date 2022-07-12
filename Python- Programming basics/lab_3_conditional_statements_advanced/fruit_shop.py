fruit = input()
day_of_week = input()
quantity = float(input())
price_of_day = 0
if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or day_of_week == 'Thursday' or day_of_week == 'Friday':
    if fruit == 'banana':
        price_of_day = (quantity * 2.50)
        print(f'{price_of_day:.2f}')
    elif fruit == 'apple':
        price_of_day = (quantity * 1.20)
        print(f'{price_of_day:.2f}')
    elif fruit == 'orange':
        price_of_day = (quantity * 0.85)
        print(f'{price_of_day:.2f}')
    elif fruit == 'grapefruit':
        price_of_day = (quantity * 1.45)
        print(f'{price_of_day:.2f}')
    elif fruit == 'kiwi':
        price_of_day = (quantity * 2.70)
        print(f'{price_of_day:.2f}')
    elif fruit == 'pineapple':
        price_of_day = (quantity * 5.50)
        print(f'{price_of_day:.2f}')
    elif fruit == 'grapes':
        price_of_day = (quantity * 3.85)
        print(f'{price_of_day:.2f}')
if day_of_week == 'Saturday' or day_of_week == 'Sunday':
    if fruit == 'banana':
        price_of_day = (quantity * 2.70)
        print(f'{price_of_day:.2f}')
    elif fruit == 'apple':
        price_of_day = (quantity * 1.25)
        print(f'{price_of_day:.2f}')
    elif fruit == 'orange':
        price_of_day = (quantity * 0.90)
        print(f'{price_of_day:.2f}')
    elif fruit == 'grapefruit':
        price_of_day = (quantity * 1.60)
        print(f'{price_of_day:.2f}')
    elif fruit == 'kiwi':
        price_of_day = (quantity * 3.00)
        print(f'{price_of_day:.2f}')
    elif fruit == 'pineapple':
        price_of_day = (quantity * 5.60)
        print(f'{price_of_day:.2f}')
    elif fruit == 'grapes':
        price_of_day = (quantity * 4.20)
        print(f'{price_of_day:.2f}')
if price_of_day == 0:
        print('error')



