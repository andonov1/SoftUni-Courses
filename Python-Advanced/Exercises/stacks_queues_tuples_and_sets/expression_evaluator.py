from collections import deque

expression = deque(input().split())
numbers = deque()

for element in expression:
    if element in '*+-/':
        while len(numbers) > 1:
            first_num = numbers.popleft()
            second_num = numbers.popleft()
            result = 0
            if element == '+':
                result = first_num + second_num
            elif element == '-':
                result = first_num - second_num
            elif element == '/' and element != 0:
                result = first_num // second_num
            else:
                result = first_num * second_num
            numbers.appendleft(result)

    else:
        numbers.append(int(element))

print(*numbers)
