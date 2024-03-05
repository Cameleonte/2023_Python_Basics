user_number = int(input())

current_number = 1
user_number_reached = False

for rows in range(1, user_number + 1):
    for columns in range(1, rows + 1):
        if current_number > user_number:
            user_number_reached = True
            break
        print(f'{current_number}', end=' ')
        current_number += 1
    if user_number_reached:
        break
    print()
