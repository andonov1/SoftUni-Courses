start = int(input())
end = int(input())
total = ''
for n in range(start, end + 1):
    total += chr(n) + ' '
print(total)