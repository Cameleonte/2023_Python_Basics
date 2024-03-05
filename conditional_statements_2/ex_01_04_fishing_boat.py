budget = int(input())
season = input()
fishermen = int(input())

ship_loan = 0

if season == 'Spring':
    ship_loan = 3000
    if fishermen <= 6:
        ship_loan *= 0.9
    elif 7 <= fishermen <= 11:
        ship_loan *= 0.85
    elif fishermen > 11:
        ship_loan *= 0.75
    elif fishermen % 2 == 0:
        ship_loan *= 0.95
elif season == 'Summer' or season == 'Autumn':
    ship_loan = 4200
    if fishermen <= 6:
        ship_loan *= 0.9
    elif 7 <= fishermen <= 11:
        ship_loan *= 0.85
    elif fishermen > 11:
        ship_loan *= 0.75
elif season == 'Winter':
    ship_loan = 2600
    if fishermen <= 6:
        ship_loan *= 0.9
    elif 7 <= fishermen <= 11:
        ship_loan *= 0.85
    elif fishermen > 11:
        ship_loan *= 0.75
    elif fishermen % 2 == 0:
        ship_loan *= 0.95
if fishermen % 2 == 0 and season != 'Autumn':
    ship_loan *= 0.95
if budget >= ship_loan:
    print(f'Yes! You have {(budget - ship_loan):.2f} leva left.')
else:
    print(f'Not enough money! You need {(ship_loan - budget):.2f} leva.')
