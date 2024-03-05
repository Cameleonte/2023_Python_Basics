from math import ceil

training_days = int(input())
first_day_distance = float(input())

current_day_distance = 0
sum_current_day_distance = 0

for day in range(1, training_days + 1):
    percent_to_raise = int(input())
    if day == 1:
        current_day_distance = first_day_distance + (first_day_distance * percent_to_raise / 100)
    else:
        current_day_distance = current_day_distance + (current_day_distance * percent_to_raise / 100)
    sum_current_day_distance += current_day_distance

tot_distance = first_day_distance + sum_current_day_distance
difference = ceil(abs(tot_distance - 1000))
if tot_distance >= 1000:
    print(f'You\'ve done a great job running {difference} more kilometers!')
else:
    print(f'Sorry Mrs. Ivanova, you need to run {difference} more kilometers')
