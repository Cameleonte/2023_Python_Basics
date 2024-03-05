film_budget = float(input())
extras_in_film = int(input())
clothing_for_extras = float(input())

set_film = film_budget * 0.1
clothing_sum = extras_in_film * clothing_for_extras

if extras_in_film > 150:
    clothing_sum = clothing_sum * 0.9

sum_needed = clothing_sum + set_film
money_needed = abs(film_budget - sum_needed)

if sum_needed > film_budget:
    print('Not enough money!')
    print(f'Wingard needs {money_needed:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {money_needed:.2f} leva left.')
