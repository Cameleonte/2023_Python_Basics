first_number = int(input())
second_number = int(input())
magical_number = int(input())

couple_counter = 0
condition = False

for i in range(first_number, second_number + 1):
    for j in range(first_number, second_number + 1):
        couple_counter += 1
        if i + j == magical_number:
            print(f'Combination N:{couple_counter} ({i} + {j} = {magical_number})')
            condition = True
            break
    if condition:
        break
else:
    print(f'{couple_counter} combinations - neither equals {magical_number}')
