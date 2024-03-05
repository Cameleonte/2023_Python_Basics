budget = float(input())
graphic_cards_count = int(input())
processors_count = int(input())
ram_count = int(input())

graphic_cards_price = graphic_cards_count * 250
processors_price = processors_count * graphic_cards_price * 0.35
ram_price = ram_count * graphic_cards_price * 0.1

tot_price = graphic_cards_price + processors_price + ram_price

if graphic_cards_count > processors_count:
    tot_price = tot_price * 0.85

sum_left = abs(budget - tot_price)

if tot_price <= budget:
    print(f'You have {sum_left:.2f} leva left!')
else:
    print(f'Not enough money! You need {sum_left:.2f} leva more!')
 