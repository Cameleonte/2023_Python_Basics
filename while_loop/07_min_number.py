from math import inf

min_number = inf

while True:
    text = input()
    if text == 'Stop':
        print(min_number)
        break
    number = int(text)
    if number < min_number:
        min_number = number
