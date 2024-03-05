season = input()
road_km = float(input())

pay_month = 0

if road_km <= 5000:
    if season == 'Spring' or season == 'Autumn':
        pay_month = road_km * 0.75
    elif season == 'Summer':
        pay_month = road_km * 0.9
    elif season == 'Winter':
        pay_month = road_km * 1.05
elif 5000 < road_km <= 10000:
    if season == 'Spring' or season == 'Autumn':
        pay_month = road_km * 0.95
    elif season == 'Summer':
        pay_month = road_km * 1.10
    elif season == 'Winter':
        pay_month = road_km * 1.25
elif 10000 < road_km <= 20000:
    pay_month = road_km * 1.45
taxed_pay = pay_month * 4 * 0.9
print(f'{taxed_pay:.2f}')
