fuel = input().lower()
lt = float(input())

if fuel == 'diesel' or fuel == 'gas' or fuel == 'gasoline':
    if lt >= 25:
        print(f'You have enough {fuel}.')
    else:
        print(f'Fill your tank with {fuel}!')
else:
    print('Invalid fuel!')
