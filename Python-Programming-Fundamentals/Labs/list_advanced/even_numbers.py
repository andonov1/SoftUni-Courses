numbers = [int(x) for x in input().split(', ')]
print([i for i in range(len(numbers)) if numbers[i] % 2 == 0])