flower_type = input()
flower_qty = int(input())
budget = int(input())
tot_sum = 0

if flower_type == 'Roses':
    tot_sum = flower_qty * 5
    if flower_qty > 80:
        tot_sum *= 0.9
elif flower_type == 'Dahlias':
    tot_sum = flower_qty * 3.8
    if flower_qty > 90:
        tot_sum *= 0.85
elif flower_type == 'Tulips':
    tot_sum = flower_qty * 2.8
    if flower_qty > 80:
        tot_sum *= 0.85
elif flower_type == 'Narcissus':
    tot_sum = flower_qty * 3
    if flower_qty < 120:
        tot_sum *= 1.15
elif flower_type == 'Gladiolus':
    tot_sum = flower_qty * 2.5
    if flower_qty < 80:
        tot_sum *= 1.2
if tot_sum <= budget:
    print(f'Hey, you have a great garden with {flower_qty} {flower_type} and {(budget - tot_sum):.2f} leva left.')
else:
    print(f'Not enough money, you need {(tot_sum - budget):.2f} leva more.')
