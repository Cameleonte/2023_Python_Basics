user_number = int(input())

print('+', end='')
for i in range(user_number - 2):
    print(' -', end='')
print(' +')
for m in range(1, user_number - 1):
    print('|', end='')
    for j in range(user_number - 2):
        print(' -', end='')
    print(' |')
print('+', end='')
for i in range(user_number - 2):
    print(' -', end='')
print(' +')

'''number = int(input())

print('*' * number)
for i in range(1, number - 1):
    k = number - 2
    print('*', end='')
    print(' ' * k, end='')
    print('*')
print('*' * number)'''