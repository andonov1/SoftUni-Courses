start = int(input())
end = int(input())
first_start = int(start / 1000)
second_start = int((start / 100) % 10)
third_start = int((start / 10) % 10)
fourth_start = int(start % 10)

first_end = int(end / 1000)
second_end = int((end / 100) % 10)
third_end = int((end / 10) % 10)
fourth_end = int(end % 10)

for num1 in range(first_start, first_end + 1):
    for num2 in range(second_start, second_end + 1):
        for num3 in range(third_start, third_end + 1):
            for num4 in range(fourth_start, fourth_end + 1):
                if num1 % 2 != 0 and \
                   num2 % 2 != 0 and \
                   num3 % 2 != 0 and \
                   num4 % 2 != 0:
                    print(f"{num1}{num2}{num3}{num4}", end=' ')

