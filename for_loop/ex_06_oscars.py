actor_name = input()
academy_points = float(input())
evaluative_num = int(input())

break_points = 1250.5
points_from_evaluations = 0

for num in range(evaluative_num):
    evaluative_name = input()
    evaluative_points = float(input())
    points_from_evaluations += len(evaluative_name) * evaluative_points / 2
    if points_from_evaluations + academy_points >= break_points:
        break
tot_points_received = academy_points + points_from_evaluations
if tot_points_received < break_points:
    difference = abs(tot_points_received - break_points)
    print(f'Sorry, {actor_name} you need {difference:.1f} more!')
else:
    print(f'Congratulations, {actor_name} got a nominee for leading role with {tot_points_received:.1f}!')
