country = ''
tot_saved_money = 0
goal_reached = False
target = False

while country != 'End':
    country = input()
    if country == 'End':
        break
    min_budget = float(input())
    while tot_saved_money < min_budget:
        saved_money = float(input())
        tot_saved_money += saved_money
    target = True
    print(f'Going to {country}!')
    tot_saved_money = 0


