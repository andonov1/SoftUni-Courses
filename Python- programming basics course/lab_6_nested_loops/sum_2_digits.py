start = int(input())
end = int(input())
magic_num = int(input())
combinations = 0
flag = False
for x1 in range(start, end + 1):
    for x2 in range(start, end + 1):
        combinations += 1
        if x1 + x2 == magic_num:
            flag = True
            print(f"Combination N:{combinations} ({x1} + {x2} = {magic_num})")
    if flag:
        break
if not flag:
    print(f"{combinations} combinations - neither equals {magic_num}")