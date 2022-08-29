numbers = [int(s) for s in input().split()]
target_num = int(input())
unique_pairs = set()
iterations = 0

for main_index in range(len(numbers)):
    for secondary_index in range(main_index+1, len(numbers)):
        iterations += 1
        if numbers[main_index] + numbers[secondary_index] == target_num:
            pair = (numbers[main_index], numbers[secondary_index])
            print(f"{numbers[main_index]} + {numbers[secondary_index]} = {target_num}")
            unique_pairs.add(pair)

print(f"Iterations done: {iterations}")
for pair in unique_pairs:
    print(pair)
