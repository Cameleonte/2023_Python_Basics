from math import inf

max_goals = - inf
best_player_name = ''
current_goals = 0
player_name = input()

while player_name != 'END':
    current_goals = int(input())
    if current_goals >= 10:
        max_goals = current_goals
        best_player_name = player_name
        break
    if current_goals > max_goals:
        max_goals = current_goals
        best_player_name = player_name
    player_name = input()

if max_goals >= 3:
    print(f'{best_player_name} is the best player!')
    print(f'He has scored {max_goals} goals and made a hat-trick !!!')
elif max_goals < 3:
    print(f'{best_player_name} is the best player!')
    print(f'He has scored {max_goals} goals.')
