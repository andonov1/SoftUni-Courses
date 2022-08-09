cards = input().split()
number_shuffles = int(input())
for shuffle in range(number_shuffles):
    last_deck = []
    middle_of_the_deck = len(cards) // 2
    left_part = cards[0:middle_of_the_deck]
    right_part = cards[middle_of_the_deck::]
    for index in range(len(left_part)):
        last_deck.append(left_part[index])
        last_deck.append(right_part[index])
    cards = last_deck
print(cards)