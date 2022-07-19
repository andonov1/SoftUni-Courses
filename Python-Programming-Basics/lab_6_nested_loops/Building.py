floors_num = int(input())
apartments_num = int(input())
apart_num = 0
apart_name = 0
for floor in range(floors_num, 0, -1):
    for apart in range(apartments_num):
        apart_num = floor * 10 + apart
        if floor == floors_num:
            apart_name = f'L{apart_num}'
        elif floor % 2 != 0:
            apart_name = f'A{apart_num}'
        else:
            apart_name = f'O{apart_num}'
        print(apart_name, end=' ')
    print()

