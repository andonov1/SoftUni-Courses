from collections import deque

boxes = [int(s) for s in input().split()]
magic = deque([int(s) for s in input().split()])
collected_presents = []
presents_dict = {}


presents = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}

while boxes and magic:
    current_box = boxes.pop()
    current_magic = magic.popleft()
    total_magic = current_magic * current_box
    if total_magic in presents:
        collected_presents.append(presents[total_magic])
    elif total_magic < 0:
        boxes.append(current_box + current_magic)
    elif total_magic > 0:
        boxes.append(current_box + 15)
    else:
        if current_box == 0 and current_magic == 0:
            continue
        if current_box == 0:
            magic.appendleft(current_magic)
        else:
            boxes.append(current_box)
task_done = False
if 'Doll' in collected_presents and 'Wooden train' in collected_presents or \
        'Teddy bear' in collected_presents and 'Bicycle' in collected_presents:
    task_done = True

if task_done:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if boxes:
    print(f"Materials left: {(', '.join([str(x) for x in reversed(boxes)]))}")
if magic:
    print(f"Magic left: {', '.join([str(x) for x in magic])}")

for present in collected_presents:
    if present not in presents_dict:
        presents_dict[present] = 1
    else:
        presents_dict[present] += 1

for key, value in sorted(presents_dict.items()):
    print(f'{key}: {value}')