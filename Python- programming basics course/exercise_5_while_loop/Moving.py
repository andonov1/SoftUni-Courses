width = int(input())
lenght = int(input())
height = int(input())
size = width * lenght * height
size_constant = size
command = input()
box_cnt = 0
while command != 'Done':
    number_boxes = int(command)
    box_cnt += number_boxes
    size -= number_boxes
    if box_cnt >= size_constant:
        diff = abs(size_constant - box_cnt)
        print(f"No more free space! You need {diff} Cubic meters more.")
        break
    command = input()
if command == 'Done' and size_constant > box_cnt:
    diff = size_constant - box_cnt
    print(f"{diff} Cubic meters left.")
