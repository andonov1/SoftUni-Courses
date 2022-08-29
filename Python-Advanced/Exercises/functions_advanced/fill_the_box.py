from collections import deque


def fill_the_box(height, length, width, *args):
    boxes_deq = deque(args)
    box_size = height * length * width
    full = False
    while boxes_deq:
        current_box = boxes_deq.popleft()
        if current_box == 'Finish':
            break
        if box_size >= current_box:
            box_size -= current_box
        else:
            full = True
            box_size -= current_box
    if not full:
        return f"There is free space in the box. You could put {box_size} more cubes."
    else:
        return f"No more free space! You have {abs(box_size)} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
