product = input()
user_output = 'unknown'

if product == 'banana' or product == 'apple' or product == 'kiwi' or product == 'cherry' or product == 'lemon'\
        or product == 'grapes':
    user_output = 'fruit'
elif product == 'tomato' or product == 'cucumber' or product == 'pepper' or product == 'carrot':
    user_output = 'vegetable'

print(user_output)
