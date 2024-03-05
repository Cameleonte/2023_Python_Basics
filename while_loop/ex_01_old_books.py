searched_book = input()

counter = 0
book_found = False
current_book = input()

while current_book != "No More Books":
    if current_book == searched_book:
        book_found = True
        break
    counter += 1
    current_book = input()
if book_found:
    print(f'You checked {counter} books and found it.')
else:
    print('The book you search is not here!')
    print(f'You checked {counter} books.')
