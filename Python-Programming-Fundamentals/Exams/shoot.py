given_nums = [int(s) for s in input().split()]
shot_targets = [[] for i in given_nums]
shot_targets_cnt = 0
while True:
    command = input()
    if command == "End":
        break
    inx = int(command)
    if 0 <= inx < len(given_nums) and shot_targets[inx] != 'shot':
        shot_targets_cnt += 1
        temp_value = given_nums[inx]
        given_nums[inx] = -1
        shot_targets[inx] = 'shot'
        for i in range(len(given_nums)):
            if shot_targets[i] != 'shot':
                if given_nums[i] > temp_value:
                    given_nums[i] -= temp_value
                else:
                    given_nums[i] += temp_value

print(f"Shot targets: {shot_targets_cnt} -> {' '.join(str(s) for s in given_nums)}")
