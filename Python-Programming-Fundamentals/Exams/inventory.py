collected_items = input().split(', ')

while True:
    command = input()
    if command == 'Craft!':
        break
    action, item = command.split(' - ')
    if action == 'Collect':
        if item not in collected_items:
            collected_items.append(item)
    elif action == 'Drop':
        if item in collected_items:
            collected_items.remove(item)
    elif action == 'Combine Items':
        old_item, new_item = item.split(':')
        if old_item in collected_items:
            inx = collected_items.index(old_item)
            collected_items.insert(inx + 1, new_item)
    else:
        if item in collected_items:
            collected_items.remove(item)
            collected_items.append(item)

print(', '.join(collected_items))