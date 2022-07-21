n = int(input())
num_is_odd = False
for i in range(n):
    num = int(input())
    if num % 2 != 0:
        num_is_odd = True
        print(f"{num} is odd!")
        break
if not num_is_odd:
    print("All numbers are even.")