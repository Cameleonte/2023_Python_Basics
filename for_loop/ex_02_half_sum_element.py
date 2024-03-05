from math import inf

number = int(input())
tot_sum = 0
max_element = -inf

for num in range(number):
    current_number = int(input())
    tot_sum += current_number
    if current_number > max_element:
        max_element = current_number
if max_element == tot_sum - max_element:
    print('Yes')
    print(f'Sum = {max_element}')
else:
    difference = abs(max_element - (tot_sum - max_element))
    print('No')
    print(f'Diff = {difference}')
