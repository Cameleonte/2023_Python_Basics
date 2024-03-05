trip_money = float(input())
money_in_hand = float(input())

past_days = 0
spend_days_counter = 0
money_collected = False

while not money_collected:
    action = input()
    amount = float(input())
    past_days += 1
    if action == 'spend':
        spend_days_counter += 1
        if spend_days_counter == 5:
            break
        money_in_hand -= amount
        if money_in_hand < 0:
            money_in_hand = 0
    elif action == 'save':
        money_in_hand += amount
        spend_days_counter = 0
        if money_in_hand >= trip_money:
            money_collected = True
if spend_days_counter == 5:
    print('You can\'t save the money.')
    print(f'{past_days}')
elif money_collected:
    print(f'You saved the money for {past_days} days.')
