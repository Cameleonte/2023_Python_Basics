days_to_stay = int(input())
room_type = input()
santa_vote = input()

night_price = 0
discount = 0

if room_type == 'room for one person':
    night_price = 18
elif room_type == 'apartment':
    night_price = 25
    if days_to_stay < 10:
        discount = 0.3
    elif days_to_stay <= 15:
        discount = 0.35
    else:
        discount = 0.5
elif room_type == 'president apartment':
    night_price = 35
    if days_to_stay < 10:
        discount = 0.1
    elif days_to_stay <= 15:
        discount = 0.15
    else:
        discount = 0.2

tot_sum = (days_to_stay - 1) * (night_price - night_price * discount)

if santa_vote == 'positive':
    tot_sum *= 1.25
elif santa_vote == 'negative':
    tot_sum *= 0.9

print(f'{tot_sum:.2f}')
