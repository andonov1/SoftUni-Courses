n = int(input())
dic = {}

for i in range(n):
    piece, composer, key = input().split('|')
    dic[piece] = [composer, key]

while True:
    command = input().split('|')
    if command[0] == 'Stop':
        break
    elif command[0] == 'Add':
        piece, composer, key = command[1:]
        if piece in dic:
            print(f"{piece} is already in the collection!")
        else:
            dic[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif command[0] == "Remove":
        piece = command[1]
        if piece in dic:
            dic.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    else:
        piece, new_key = command[1:]
        if piece in dic:
            dic[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for key, value in dic.items():
    print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")
