first_number_limit = int(input())
second_number_limit = int(input())
third_number_limit = int(input())

for num1 in range(1, first_number_limit + 1):
    for num2 in range(1, second_number_limit + 1):
        for num3 in range(1, third_number_limit + 1):
            if num3 % 2 == 0 and (num2 == 2 or num2 == 3 or num2 == 5 or num2 == 7) and num1 % 2 == 0:
                print(f'{num1} {num2} {num3}')
