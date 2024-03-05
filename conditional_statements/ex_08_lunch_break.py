from math import ceil

serial_name = input()
episode_time = int(input())
rest_time = int(input())

lunch_time = rest_time / 8
free_time = rest_time / 4
left_time = rest_time - lunch_time - free_time
minutes = (abs(left_time - episode_time))
rounded_minutes = ceil(minutes)

if left_time >= episode_time:
    print(f'You have enough time to watch {serial_name} and left with {rounded_minutes} minutes free time.')
else:
    print(f"You don't have enough time to watch {serial_name}, you need {rounded_minutes} more minutes.")
