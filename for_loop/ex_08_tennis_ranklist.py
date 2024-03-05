from math import floor

tournaments_number = int(input())
initial_points = int(input())

points_received = 0
tournaments_won = 0

for num in range(tournaments_number):
    tournament_stage = input()
    if tournament_stage == 'W':
        points_received += 2000
        tournaments_won += 1
    elif tournament_stage == 'F':
        points_received += 1200
    elif tournament_stage == 'SF':
        points_received += 720

tot_points_received = points_received + initial_points
average_points = points_received / tournaments_number
percent_tournaments_won = tournaments_won / tournaments_number * 100
print(f'Final points: {tot_points_received}')
print(f'Average points: {floor(average_points)}')
print(f'{percent_tournaments_won:.2f}%')
