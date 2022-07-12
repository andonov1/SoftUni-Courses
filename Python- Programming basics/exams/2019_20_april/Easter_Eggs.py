import sys
red = 0
orange = 0
blue = 0
green = 0
max_eggs = -sys.maxsize
max_eggs_colour = ''
num_eggs = int(input())
for i in range(num_eggs):
    current_colour = input()
    if current_colour == 'red':
        red += 1
        if red >= max_eggs:
            max_eggs = red
            max_eggs_colour = 'red'
    elif current_colour == 'orange':
        orange += 1
        if orange >= max_eggs:
            max_eggs = orange
            max_eggs_colour = 'orange'
    elif current_colour == 'blue':
        blue += 1
        if blue >= max_eggs:
            max_eggs = blue
            max_eggs_colour = 'blue'
    elif current_colour == 'green':
        green += 1
        if green >= max_eggs:
            max_eggs = green
            max_eggs_colour = 'green'
print(f"Red eggs: {red}")
print(f"Orange eggs: {orange}")
print(f"Blue eggs: {blue}")
print(f"Green eggs: {green}")
print(f"Max eggs: {max_eggs} -> {max_eggs_colour}")
