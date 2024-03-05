n = int(input())

for row in range(1, n + 1):
    for column in range(1, n - row + 1):
        print(' ', end='')
    print('*', end='')
    for column in range(1, row):
        print(' *', end='')
    print()
for row in range(n, 1, - 1):
    for column in range(1, row):
        print(' *', end='')
    print()
    for column in range(1, n + 1 - row + 1):
        print(' ', end='')
