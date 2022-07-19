favourite_book = input()
cnt_books = 0
current_book = input()
is_found = False

while current_book != 'No More Books':
    if current_book == favourite_book:
        is_found = True
        break
    cnt_books += 1
    current_book = input()
if is_found:
    print(f'You checked {cnt_books} books and found it.')
else:
    print("The book you search is not here!")
    print(f"You checked {cnt_books} books.")

