def is_valid(row, col):
    if 0 <= row < 8 and 0 <= col < 8:
        return True
    else:
        return False


board = []
columns = {0: 'a',
           1: 'b',
           2: 'c',
           3: 'd',
           4: 'e',
           5: 'f',
           6: 'g',
           7: 'h'}
rows = {0: '8',
        1: '7',
        2: '6',
        3: '5',
        4: '4',
        5: '3',
        6: '2',
        7: '1'}
turn = 0
white_row, white_col = None, None
black_row, black_col = None, None
for i in range(8):
    board.append([s for s in input().split()])
    for j in range(8):
        if board[i][j] == 'w':
            white_row, white_col = i, j
        if board[i][j] == 'b':
            black_row, black_col = i, j

while True:
    if turn % 2 == 0:
        board[white_row][white_col] = '-'
        if is_valid(white_row - 1, white_col - 1):
            if board[white_row - 1][white_col - 1] == 'b':
                board[white_row - 1][white_col - 1] = 'w'
                print(f"Game over! White win, capture on {columns[white_col - 1]}{rows[white_row - 1]}.")
                break
        if is_valid(white_row - 1, white_col + 1):
            if board[white_row - 1][white_col + 1] == 'b':
                board[white_row - 1][white_col + 1] = 'w'
                print(f"Game over! White win, capture on {columns[white_col + 1]}{rows[white_row - 1]}.")
                break
        else:
            board[white_row - 1][white_col] = 'w'
            white_row, white_col = white_row - 1, white_col
            if white_row == 0:
                print(f"Game over! White pawn is promoted to a queen at {columns[white_col]}{rows[white_row]}.")
                break
    else:
        board[black_row][black_col] = '-'

        if is_valid(black_row + 1, black_col - 1):
            if board[black_row + 1][black_col - 1] == 'w':
                board[black_row + 1][black_col - 1] = 'b'
                print(f"Game over! Black win, capture on {columns[black_col - 1]}{rows[black_row + 1]}.")
                break
        if is_valid(black_row + 1, black_col + 1):
            if board[black_row + 1][black_col + 1] == 'w':
                board[black_row + 1][black_col + 1] = 'b'
                print(f"Game over! Black win, capture on {columns[black_col + 1]}{rows[black_row + 1]}.")
                break
        else:
            board[black_row + 1][black_col] = 'b'
            black_row, black_col = black_row + 1, black_col
            if black_row == 7:
                print(f"Game over! White pawn is promoted to a queen at {columns[black_col]}{rows[black_row]}.")
                break
    turn += 1
