n_number = int(input())
found_num = False
cnt = 0
for a in range(1, 9 + 1):
    for b in range(9, a, -1):
        for c in range(0, 9 + 1):
            for d in range(9, c, -1):
                num_sum = a + b + c + d
                num_multiplied = a * b * c * d
                if num_sum == num_multiplied and n_number % 10 == 5:
                    cnt += 1
                    print(f'{a}{b}{c}{d}')
                    found_num = True
                    break
                if num_multiplied // num_sum == 3 and n_number % 3 == 0:
                    cnt += 1
                    print(f'{d}{c}{b}{a}')
                    found_num = True
                    break
            if found_num:
                break
        if found_num:
            break
    if found_num:
        break
if cnt == 0:
    print("Nothing found")