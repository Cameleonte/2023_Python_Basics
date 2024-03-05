number = int(input())

for rows in range(1, number + 1):
    for columns in range(1, number + 1):
        if columns > rows:
            break
        print('$', end=' ')
    print()

'''
symbol = input('Please input the symbol that you\'d like to use: ')
lines = int(input('Please insert the number of lines that you want to draw: '))

for row in range(1, lines + 1):
    for column in range(1, row + 1):
        print(f'{symbol}', end=' ')
    print()
'''
