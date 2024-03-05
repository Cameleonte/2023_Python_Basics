km = int(input())
period = input()

sum_bus = 0.09 * km
sum_train = 0.06 * km
sum_taxi_n = 0.7 + (0.9 * km)
sum_taxi_d = 0.7 + (0.79 * km)

if km < 20:
    if period == 'day':
        print(f'{sum_taxi_d:.2f}')
    else:
        print(f'{sum_taxi_n:.2f}')
elif km < 100:
    print(f'{sum_bus:.2f}')
elif km >= 100:
    print(f'{sum_train:.2f}')
