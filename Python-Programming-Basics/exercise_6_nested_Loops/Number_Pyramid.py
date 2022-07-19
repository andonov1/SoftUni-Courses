n = int(input())
cnt = 1
pyramid_is_true = False
for row in range(1, n + 1):
    for col in range(0, row):
        print(f'{cnt}', end=' ')
        cnt += 1
        if cnt > n:
            pyramid_is_true = True
            break
    if pyramid_is_true:
        break
    print()