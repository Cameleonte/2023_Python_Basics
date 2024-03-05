town = input()
volume = float(input())
commission = 0
is_valid = True

if town == 'Sofia':
    if 0 <= volume <= 500:
        commission = 0.05
    elif 500 < volume <= 1000:
        commission = 0.07
    elif 1000 < volume <= 10000:
        commission = 0.08
    elif volume > 10000:
        commission = 0.12
    else:
        is_valid = False
elif town == 'Varna':
    if 0 <= volume <= 500:
        commission = 0.045
    elif 500 < volume <= 1000:
        commission = 0.075
    elif 1000 < volume <= 10000:
        commission = 0.1
    elif volume > 10000:
        commission = 0.13
    else:
        is_valid = False
elif town == 'Plovdiv':
    if 0 <= volume <= 500:
        commission = 0.055
    elif 500 < volume <= 1000:
        commission = 0.08
    elif 1000 < volume <= 10000:
        commission = 0.12
    elif volume > 10000:
        commission = 0.145
    else:
        is_valid = False
else:
    is_valid = False

if is_valid:
    print(f'{commission * volume:.2f}')
else:
    print('error')
