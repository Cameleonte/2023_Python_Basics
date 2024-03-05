product = input()
town = input()
quantity = float(input())

user_output = 0

if town == 'Sofia':
    if product == 'coffee':
        user_output = 0.5 * quantity
    elif product == 'water':
        user_output = 0.8 * quantity
    elif product == 'beer':
        user_output = 1.2 * quantity
    elif product == 'sweets':
        user_output = 1.45 * quantity
    elif product == 'peanuts':
        user_output = 1.6 * quantity
elif town == 'Plovdiv':
    if product == 'coffee':
        user_output = 0.4 * quantity
    elif product == 'water':
        user_output = 0.7 * quantity
    elif product == 'beer':
        user_output = 1.15 * quantity
    elif product == 'sweets':
        user_output = 1.30 * quantity
    elif product == 'peanuts':
        user_output = 1.5 * quantity
elif town == 'Varna':
    if product == 'coffee':
        user_output = 0.45 * quantity
    elif product == 'water':
        user_output = 0.7 * quantity
    elif product == 'beer':
        user_output = 1.1 * quantity
    elif product == 'sweets':
        user_output = 1.35 * quantity
    elif product == 'peanuts':
        user_output = 1.55 * quantity

print(user_output)
