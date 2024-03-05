tot_sum = 0

while True:
    text = input()
    if text == 'NoMoreMoney':
        break

    current_sum = float(text)
    if current_sum >= 0:
        tot_sum += current_sum
        print(f'Increase: {current_sum:.2f}')
    else:
        print('Invalid operation!')
        break

print(f'Total: {tot_sum:.2f}')
