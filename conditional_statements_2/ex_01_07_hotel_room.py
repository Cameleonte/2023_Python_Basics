month = input()
nights = int(input())

tot_price_studio = 0
tot_price_apartment = 0

if month == 'May' or month == 'October':
    if nights <= 7:
        tot_price_apartment = nights * 65
        tot_price_studio = nights * 50
    elif nights <= 14:
        tot_price_apartment = nights * 65
        tot_price_studio = nights * 50 * 0.95
    else:
        tot_price_apartment = nights * 65 * 0.9
        tot_price_studio = nights * 50 * 0.7
elif month == 'June' or month == 'September':
    if nights <= 14:
        tot_price_apartment = nights * 68.7
        tot_price_studio = nights * 75.2
    else:
        tot_price_apartment = nights * 68.7 * 0.9
        tot_price_studio = nights * 75.2 * 0.8
elif month == 'July' or month == 'August':
    tot_price_studio = nights * 76
    if nights > 14:
        tot_price_apartment = nights * 77 * 0.9
    else:
        tot_price_apartment = nights * 77
print(f'Apartment: {tot_price_apartment:.2f} lv.')
print(f'Studio: {tot_price_studio:.2f} lv.')
