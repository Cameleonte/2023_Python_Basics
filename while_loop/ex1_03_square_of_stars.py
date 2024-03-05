number = int(input())

for rows in range(1, number + 1):
    for columns in range(1, number + 1):
        print(f'*', end=' ')
    print()
