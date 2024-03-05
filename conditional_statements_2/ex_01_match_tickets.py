budget = float(input())
category = input()
fans = int(input())

ticket_price = 0
percent = 0
tot_tickets_price = fans * ticket_price
money_left_for_tickets = budget - percent * budget
tot_money_left = abs(tot_tickets_price - money_left_for_tickets)

if category == 'VIP':
    ticket_price = 499.99
    if fans <= 4:
        percent = 0.75
    elif fans <= 9:
        percent = 0.6
    elif fans <= 24:
        percent = 0.5
    elif fans <= 49:
        percent = 0.4
    elif fans > 50:
        percent = 0.25
    tot_tickets_price = fans * ticket_price
    money_left_for_tickets = budget - percent * budget
    tot_money_left = abs(tot_tickets_price - money_left_for_tickets)
elif category == 'Normal':
    ticket_price = 249.99
    if fans <= 4:
        percent = 0.75
    elif fans <= 9:
        percent = 0.6
    elif fans <= 24:
        percent = 0.5
    elif fans <= 49:
        percent = 0.4
    elif fans > 50:
        percent = 0.25
    tot_tickets_price = fans * ticket_price
    money_left_for_tickets = budget - percent * budget
    tot_money_left = abs(tot_tickets_price - money_left_for_tickets)
if tot_tickets_price < money_left_for_tickets:
    print(f'Yes! You have {tot_money_left:.2f} leva left.')
else:
    print(f'Not enough money! You need {tot_money_left:.2f} leva.')
