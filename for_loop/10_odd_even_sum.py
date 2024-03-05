user_input = int(input())

total_even = 0
total_odd = 0

for num in range(user_input):
    current_number = int(input())
    if num % 2 == 0:
        total_even += current_number
    else:
        total_odd += current_number
if total_even == total_odd:
    print('Yes')
    print(f'Sum = {total_even}')
else:
    difference = abs(total_even - total_odd)
    print('No')
    print(f'Diff = {difference}')
