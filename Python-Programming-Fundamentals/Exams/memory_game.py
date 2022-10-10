seq = input().split()
cnt_moves = 0

while True:
    command = input()
    if command == 'end':
        break
    command = command.split()
    first_num, second_num = int(command[0]), int(command[1])
    cnt_moves += 1
    if first_num == second_num or first_num < 0 or first_num >= len(seq) or second_num < 0 \
            or second_num >= len(seq):
        seq.insert(len(seq) // 2, f"-{str(cnt_moves)}a")
        seq.insert(len(seq) // 2, f"-{str(cnt_moves)}a")
        print("Invalid input! Adding additional elements to the board")
        continue
    if seq[first_num] == seq[second_num]:
        print(f"Congrats! You have found matching elements - {seq[first_num]}!")
        x = seq.pop(first_num)
        seq.remove(x)

    elif seq[first_num] != seq[second_num]:
        print("Try again!")

    if len(seq) < 1:
        print(f"You have won in {cnt_moves} turns!")
        break

if len(seq) > 0:
    print(f"Sorry you lose :("
          f"\n{' '.join(seq)}")


