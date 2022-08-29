from collections import deque

given_string = deque(input().split())
main_colours = ["red", "yellow", "blue"]
secondary_colours = ["orange", "purple", "green"]
collected_colours = []
final_colours = []

while given_string:
    first_substring = given_string.popleft()
    last_substring = given_string.pop() if given_string else ''
    result = first_substring + last_substring
    if result in main_colours or result in secondary_colours:
        collected_colours.append(result)
        continue
    result = last_substring + first_substring
    if result in main_colours or result in secondary_colours:
        collected_colours.append(result)
        continue

    first_substring = first_substring[:-1]
    last_substring = last_substring[:-1]
    if first_substring:
        if len(given_string) % 2 == 0:
            given_string.insert(int(len(given_string) / 2), first_substring)
        else:
            given_string.insert(int(len(given_string) / 2) + 1, first_substring)
    if last_substring:
        if len(given_string) % 2 == 0:
            given_string.insert(int(len(given_string) / 2), last_substring)
        else:
            given_string.insert(int(len(given_string) / 2) + 1, last_substring)

for colour in collected_colours:
    if colour == 'orange':
        if 'red' in collected_colours and 'yellow' in collected_colours:
            final_colours.append(colour)
    elif colour == 'purple':
        if 'red' in collected_colours and 'blue' in collected_colours:
            final_colours.append(colour)
    elif colour == 'green':
        if 'yellow' in collected_colours and 'blue' in collected_colours:
            final_colours.append(colour)
    else:
        final_colours.append(colour)

print(final_colours)