from math import inf

user_input = int(input())

max_odd_number = - inf
min_odd_number = inf
max_even_number = - inf
min_even_number = inf
even_sum = 0
odd_sum = 0

for i in range(1, user_input + 1):
    current_number = float(input())
    if i % 2 != 0:
        odd_sum += current_number
        if current_number > max_odd_number:
            max_odd_number = current_number
        if current_number <= min_odd_number:
            min_odd_number = current_number
    else:
        even_sum += current_number
        if current_number > max_even_number:
            max_even_number = current_number
        if current_number <= min_even_number:
            min_even_number = current_number
print(f'OddSum={odd_sum:.2f},')
if min_odd_number == inf:
    min_odd_number = 'No'
    print('OddMin=%.2s,' % min_odd_number)
else:
    print(f'OddMin={min_odd_number:.2f},')
if max_odd_number == - inf:
    max_odd_number = 'No'
    print(f'OddMax=%.2s,' % max_odd_number)
else:
    print(f'OddMax={max_odd_number:.2f},')
print(f'EvenSum={even_sum:.2f},')
if min_even_number == inf:
    min_even_number = 'No'
    print('EvenMin=%.2s,' % min_even_number)
else:
    print(f'EvenMin={min_even_number:.2f},')
if max_even_number == - inf:
    max_even_number = 'No'
    print('EvenMax=%.2s' % max_even_number)
else:
    print(f'EvenMax={max_even_number:.2f}')
