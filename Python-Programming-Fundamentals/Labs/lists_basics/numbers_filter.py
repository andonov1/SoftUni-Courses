n = int(input())
positive_nums = []
negative_nums = []
even_nums = []
odd_nums = []

for _ in range(n):
    curr_num = int(input())
    if curr_num >= 0:
        positive_nums.append(curr_num)
    if curr_num < 0:
        negative_nums.append(curr_num)
    if curr_num % 2 == 0:
        even_nums.append(curr_num)
    if curr_num % 2 != 0:
        odd_nums.append(curr_num)
command = input()
if command == 'even':
    print(even_nums)
elif command == 'odd':
    print(odd_nums)
elif command == 'positive':
    print(positive_nums)
else:
    print(negative_nums)
