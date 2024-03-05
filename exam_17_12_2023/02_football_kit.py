t_shirt_price = float(input())
gift_sum = float(input())

shorts_price = 0.75 * t_shirt_price
socks_price = 0.2 * shorts_price
soccer_cleats_price = 2 * (t_shirt_price + shorts_price)
tot_sum = t_shirt_price + shorts_price + socks_price + soccer_cleats_price
sum_to_pay = 0.85 * tot_sum

if sum_to_pay >= gift_sum:
    print(f'Yes, he will earn the world-cup replica ball!')
    print(f'His sum is {sum_to_pay:.2f} lv.')
else:
    difference = gift_sum - sum_to_pay
    print(f'No, he will not earn the world-cup replica ball.')
    print(f'He needs {difference:.2f} lv. more.')
