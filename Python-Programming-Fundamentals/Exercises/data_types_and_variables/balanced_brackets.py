n_lines = int(input())
open_brackets = 0
closed_brackets = 0
flag = True
for i in range(n_lines):
    command = input()
    if command == '(':
        open_brackets += 1
    if command == ')':
        closed_brackets += 1
    if open_brackets > closed_brackets + 1 or closed_brackets > open_brackets:
        flag = False

if not flag:
    print('UNBALANCED')
else:
    print(f'BALANCED')

