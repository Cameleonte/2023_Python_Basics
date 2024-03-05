rest_days = int(input())
room_type = input()
vote = input()

room_price = 0
nights = rest_days - 1

if room_type == 'room for one person':
    room_price = 18
elif room_type == 'apartment':
    room_price = 25
    if rest_days < 10:
        room_price *= 0.7
    elif rest_days <= 15:
        room_price *= 0.65
    else:
        room_price *= 0.5
elif room_type == 'president apartment':
    room_price = 35
    if rest_days < 10:
        room_price *= 0.9
    elif rest_days <= 15:
        room_price *= 0.85
    else:
        room_price *= 0.8
tot_sum = room_price * nights
if vote == 'positive':
    tot_sum *= 1.25
elif vote == 'negative':
    tot_sum *= 0.9
print(f'{tot_sum:.2f}')
