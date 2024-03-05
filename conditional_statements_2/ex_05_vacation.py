budget = float(input())
season = input()

expense = 0
location = ''
place = ''

if budget <= 1000:
    location = 'Camp'
    if season == 'Summer':
        expense = budget * 0.65
        place = 'Alaska'
    elif season == 'Winter':
        expense = budget * 0.45
        place = 'Morocco'
elif budget <= 3000:
    location = 'Hut'
    if season == 'Summer':
        expense = budget * 0.8
        place = 'Alaska'
    elif season == 'Winter':
        expense = budget * 0.6
        place = 'Morocco'
elif budget > 3000:
    location = 'Hotel'
    expense = budget * 0.9
    if season == 'Summer':
        place = 'Alaska'
    elif season == 'Winter':
        place = 'Morocco'
print(f'{place} - {location} - {expense:.2f}')
