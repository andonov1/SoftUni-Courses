notes = [0] * 10
command = input()

while command != 'End':
    importance, note = command.split('-')
    current_index = int(importance) - 1
    notes[current_index] = note
    command = input()
print([x for x in notes if x != 0])
