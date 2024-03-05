sum_prime_numbers = 0
sum_non_prime_numbers = 0
command = input()

while command != 'stop':
    user_number = int(command)
    if user_number < 0:
        print('Number is negative.')
    else:
        user_number_is_prime = True
        for number in range(2, user_number):
            if user_number % number == 0:
                user_number_is_prime = False
                break
        if user_number_is_prime:
            sum_prime_numbers += user_number
        else:
            sum_non_prime_numbers += user_number
    command = input()
print(f'Sum of all prime numbers is: {sum_prime_numbers}')
print(f'Sum of all non prime numbers is: {sum_non_prime_numbers}')
