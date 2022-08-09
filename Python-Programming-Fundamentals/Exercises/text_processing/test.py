tickets = [i.strip() for i in input().split(', ')]
winning_symbols = ['@', '#', '$', '^']
for ticket in tickets:
    if len(ticket) != 20:
        print("invalid ticket")
    else:
        both_sides_correct = False
        left_side_symbols = ''
        for i in range(10):
            if ticket[i] in winning_symbols:
                left_side_symbols += ticket[i]
                if ticket[i + 1] not in winning_symbols:
                    break
        if left_side_symbols in ticket[10:20]:
            both_sides_correct = True
            current_lenght = left_side_symbols
        else:
            for i in range(len(left_side_symbols), 0, -1):
                current_lenght = left_side_symbols[i:len(left_side_symbols)]
                if current_lenght in ticket[10:20]:
                    both_sides_correct = True
                    break
        if both_sides_correct and len(current_lenght) == 10:
            print(f'ticket "{ticket}" - {len(current_lenght)}{current_lenght[0]} Jackpot!')
        if both_sides_correct and len(current_lenght) < 6:
            print(f'ticket "{ticket}" - no match')
        if both_sides_correct and 10 > len(current_lenght) >= 6:
            print(f'ticket "{ticket}" - {len(current_lenght)}{current_lenght[0]}')
