budget = float(input())
season = input()
car_class = ''
price = 0
car_type = ''

if budget <= 100:
    car_class = 'Economy class'
    if season == 'Summer':
        price = budget * 0.35
        car_type = 'Cabrio'
    elif season == "Winter":
        price = budget * 0.65
        car_type = 'Jeep'
elif 100 < budget <= 500:
    car_class = 'Compact class'
    if season == 'Summer':
        price = budget * 0.45
        car_type = 'Cabrio'
    elif season == "Winter":
        price = budget * 0.8
        car_type = 'Jeep'
elif budget > 500:
    car_class = 'Luxury class'
    if season == 'Summer' or season == 'Winter':
        price = budget * 0.9
        car_type = 'Jeep'

print(car_class)
print(f'{car_type} - {price:.2f}')
