user_number = int(input())

special_number = 0
for current_number in range(1111, 9999 + 1):
    symbols = str(current_number)
    number_divides = True
    for index in symbols:
        if int(index) == 0 or user_number % int(index) != 0:
            number_divides = False
            break
        else:
            special_number = int(symbols)
    if number_divides:
        print(f'{special_number}', end=' ')
