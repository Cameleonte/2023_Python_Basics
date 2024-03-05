lili_age = int(input())
laundry_price = float(input())
toy_price = int(input())

toys = 0
sum_collected = 0
brother_help = 0

for birthday in range(1, lili_age + 1):
    if birthday % 2 == 0:
        sum_collected += 10 * birthday / 2
        brother_help += 1
    else:
        toys += 1
sum_toys = toys * toy_price
tot_sum = sum_toys + sum_collected - brother_help
difference = abs(tot_sum - laundry_price)
if tot_sum >= laundry_price:
    print(f'Yes! {difference:.2f}')
else:
    print(f'No! {difference:.2f}')
