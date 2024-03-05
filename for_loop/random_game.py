import random

print('-----***** Welcome to the "Guess the number" game! *****-----')
print('I\'ve selected a random number between 1 and 100. Try to guess it!')

secret_number = random.randint(1, 100)

for attempt in range(1, 6):
    guess = int(input('Please enter your guess: '))

    if guess == secret_number:
        print(f'Congratulations! You guessed the correct number in {attempt} attempts.')
        break

    elif guess < secret_number:
        print('Sorry! Too low, try again.')

    else:
        print('Sorry! Too high, try again.')

print(f'The right number is {secret_number}')
print('Hope you\'re enjoying the game!')
