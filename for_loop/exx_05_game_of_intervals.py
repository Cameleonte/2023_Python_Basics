moves_count = int(input())

tot_result = 0
sum_invalid = 0
sum_to_9 = 0
sum_to_19 = 0
sum_to_29 = 0
sum_to_39 = 0
sum_to_50 = 0
for num in range(moves_count):
    current_number = int(input())
    if 0 <= current_number <= 9:
        tot_result += 0.2 * current_number
        sum_to_9 += 1
    elif 10 <= current_number <= 19:
        tot_result += 0.3 * current_number
        sum_to_19 += 1
    elif 20 <= current_number <= 29:
        tot_result += 0.4 * current_number
        sum_to_29 += 1
    elif 30 <= current_number <= 39:
        tot_result += 50
        sum_to_39 += 1
    elif 40 <= current_number <= 50:
        tot_result += 100
        sum_to_50 += 1
    else:
        tot_result /= 2
        sum_invalid += 1
percent_to_9 = sum_to_9 / moves_count * 100
percent_to_19 = sum_to_19 / moves_count * 100
percent_to_29 = sum_to_29 / moves_count * 100
percent_to_39 = sum_to_39 / moves_count * 100
percent_to_50 = sum_to_50 / moves_count * 100
percent_invalid = sum_invalid / moves_count * 100
print(f'{tot_result:.2f}')
print(f'From 0 to 9: {percent_to_9:.2f}%')
print(f'From 10 to 19: {percent_to_19:.2f}%')
print(f'From 20 to 29: {percent_to_29:.2f}%')
print(f'From 30 to 39: {percent_to_39:.2f}%')
print(f'From 40 to 50: {percent_to_50:.2f}%')
print(f'Invalid numbers: {percent_invalid:.2f}%')
