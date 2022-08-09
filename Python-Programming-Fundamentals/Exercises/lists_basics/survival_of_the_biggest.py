numbers = input().split()
integer_nums = []
cnt_number_to_remove = int(input())
biggest_nums = []
for i in numbers:
    integer_nums.append(int(i))
for _ in range(cnt_number_to_remove):
    integer_nums.remove(min(integer_nums))
for i in integer_nums:
    biggest_nums.append(i)
for i in range(len(integer_nums)):
    if i < len(integer_nums) - 1:
        print(f"{integer_nums[i]}, ", end='')
    else:
        print(f'{integer_nums[i]}', end='')
