version = [int(i) for i in input().split('.')]
version[-1] += 1
for i in range(len(version) - 1, -1, -1):
    if version[i] > 9:
        version[i] = 0
        version[i - 1] += 1
print('.'.join(str(n) for n in version))


