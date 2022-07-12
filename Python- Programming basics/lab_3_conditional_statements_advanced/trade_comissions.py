city = input()
volume = float(input())
rate = 0
if city == 'Sofia':
    if 0 <= volume <= 500:
        rate = 0.05
    elif 500 <= volume <= 1000:
        rate = 0.07
    elif 1000 <= volume <= 10000:
        rate = 0.08
    elif volume > 10000:
        rate = 0.12
elif city == 'Varna':
    if 0 <= volume <= 500:
        rate = 0.045
    elif 500 <= volume <= 1000:
        rate = 0.075
    elif 1000 <= volume <= 10000:
        rate = 0.10
    elif volume > 10000:
        rate = 0.13
elif city == 'Plovdiv':
    if 0 <= volume <= 500:
        rate = 0.055
    elif 500 <= volume <= 1000:
        rate = 0.08
    elif 1000 <= volume <= 10000:
        rate = 0.12
    elif volume > 10000:
        rate = 0.145
if rate > 0:
    print(f'{volume * rate:.2f}')
if rate == 0:
    print('error')