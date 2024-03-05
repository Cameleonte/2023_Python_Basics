first_user_number = int(input())
second_user_number = int(input())

current_str_number = ''

for current_number in range(first_user_number, second_user_number + 1):
    current_str_number = str(current_number)
    even_sum = 0
    odd_sum = 0
    for index, digit in enumerate(current_str_number):
        if index % 2 == 0:
            odd_sum += int(digit)
        else:
            even_sum += int(digit)
    if even_sum == odd_sum:
        print(current_number, end=' ')
