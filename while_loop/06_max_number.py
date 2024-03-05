from math import inf

max_num = - inf

while True:
    text = input()
    if text == 'Stop':
        print(max_num)
        break
    number = int(text)
    if number > max_num:
        max_num = number
