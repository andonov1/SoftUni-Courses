import sys


def memorized_fibonacci(number, memo):
    if number not in memo:
        memo[number] = memorized_fibonacci(number - 1, memo) + memorized_fibonacci(number - 2, memo)
    return memo[number]


memorized = {1: 0, 2: 1, 3: 1}

print(memorized_fibonacci(50, memorized))
start_num = int(sys.argv[1])
end_num = int(sys.argv[2])
result = []
for i in range(start_num, end_num + 1):
    result.append(memorized_fibonacci(i, memorized))

print(result)
