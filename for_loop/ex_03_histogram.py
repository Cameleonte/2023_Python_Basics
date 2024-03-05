user_input = int(input())
number1 = 0
number2 = 0
number3 = 0
number4 = 0
number5 = 0

for i in range(user_input):
    current_number = int(input())

    if current_number < 200:
        number1 += 1
    if 200 <= current_number < 400:
        number2 += 1
    if 400 <= current_number < 600:
        number3 += 1
    if 600 <= current_number < 800:
        number4 += 1
    if 800 <= current_number <= 1000:
        number5 += 1
number1_percent = number1 / user_input * 100
number2_percent = number2 / user_input * 100
number3_percent = number3 / user_input * 100
number4_percent = number4 / user_input * 100
number5_percent = number5 / user_input * 100

print(f'{number1_percent:.2f}%')
print(f'{number2_percent:.2f}%')
print(f'{number3_percent:.2f}%')
print(f'{number4_percent:.2f}%')
print(f'{number5_percent:.2f}%')
