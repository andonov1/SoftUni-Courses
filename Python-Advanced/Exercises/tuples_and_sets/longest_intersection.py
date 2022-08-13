def gen_seq(range_info):
    start, end = [int(x) for x in range_info.split(',')]
    return set(range(start, end + 1))


n = int(input())
longest_intersection = []

for _ in range(n):
    line_parts = input().split('-')
    first_set = gen_seq(line_parts[0])
    second_set = gen_seq(line_parts[1])
    current_intersection = first_set.intersection(second_set)
    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection


print(f"Longest intersection is [{', '.join([str(s) for s in longest_intersection])}] with length {len(longest_intersection)}")