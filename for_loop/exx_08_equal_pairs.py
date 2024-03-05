from math import inf

couple_numbers = int(input())

sum_numbers = 0
equal_sum_numbers = 0
difference = 0
max_diff = - inf

for num in range(1, couple_numbers + 1):
    if num == 1:
        current_number_1 = int(input())
        current_number_2 = int(input())
        sum_numbers = current_number_1 + current_number_2
    if num == couple_numbers:
        break
    next_current_number_1 = int(input())
    next_current_number_2 = int(input())
    current_sum_numbers = next_current_number_1 + next_current_number_2
    difference = abs(current_sum_numbers - sum_numbers)
    if difference != 0:
        sum_numbers = current_sum_numbers
        max_diff = difference
    else:
        equal_sum_numbers += 1
    if num == couple_numbers - 1:
        break
if difference == 0:
    print(f'Yes, value={sum_numbers}')
else:
    print(f'No, maxdiff={max_diff}')
