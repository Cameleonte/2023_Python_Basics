fuel = input()
fuel_quantity = float(input())
card = input()

tot_spent = 0

if fuel == 'Gasoline' and card == 'No':
    gasoline_price = 2.22
    tot_spent = fuel_quantity * gasoline_price
    if 20 <= fuel_quantity <= 25:
        tot_spent *= 0.92
    elif fuel_quantity > 25:
        tot_spent *= 0.9
elif fuel == 'Diesel' and card == 'No':
    diesel_price = 2.33
    tot_spent = fuel_quantity * diesel_price
    if 20 <= fuel_quantity <= 25:
        tot_spent *= 0.92
    elif fuel_quantity > 25:
        tot_spent *= 0.9
elif fuel == 'Gas' and card == 'No':
    gas_price = 0.93
    tot_spent = fuel_quantity * gas_price
    if 20 <= fuel_quantity <= 25:
        tot_spent *= 0.92
    elif fuel_quantity > 25:
        tot_spent *= 0.9
elif fuel == 'Gasoline' and card == 'Yes':
    gasoline_price = 2.04
    tot_spent = fuel_quantity * gasoline_price
    if 20 <= fuel_quantity <= 25:
        tot_spent *= 0.92
    elif fuel_quantity > 25:
        tot_spent *= 0.9
elif fuel == 'Diesel' and card == 'Yes':
    diesel_price = 2.21
    tot_spent = fuel_quantity * diesel_price
    if 20 <= fuel_quantity <= 25:
        tot_spent *= 0.92
    elif fuel_quantity > 25:
        tot_spent *= 0.9
elif fuel == 'Gas' and card == 'Yes':
    gas_price = 0.85
    tot_spent = fuel_quantity * gas_price
    if 20 <= fuel_quantity <= 25:
        tot_spent *= 0.92
    elif fuel_quantity > 25:
        tot_spent *= 0.9

print(f'{tot_spent:.2f} lv.')
