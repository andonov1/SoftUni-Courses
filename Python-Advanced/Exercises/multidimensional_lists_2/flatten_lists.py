lists = input().split('|')
flatten_list = []
for i in range(len(lists)):
    current_list = lists.pop().split()
    for num in current_list:
        flatten_list.append(num)
print(*flatten_list)
