from math import inf

number = int(input())
max_number = - inf
min_number = inf

for num in range(number):
    user_input = int(input())
    if user_input > max_number:
        max_number = user_input
    if user_input < min_number:
        min_number = user_input

print(f'Max number: {max_number}')
print(f'Min number: {min_number}')
