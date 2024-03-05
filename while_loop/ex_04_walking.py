target_steps = 10000
tot_steps_made = 0

while tot_steps_made < target_steps:
    text = input()
    if text == 'Going home':
        steps_returning_home = int(input())
        tot_steps_made += steps_returning_home
        break
    current_steps_made = int(text)
    tot_steps_made += current_steps_made
difference = abs(tot_steps_made - target_steps)
if tot_steps_made >= target_steps:
    print(f'Goal reached! Good job!')
    print(f'{difference} steps over the goal!')
else:
    print(f'{difference} more steps to reach goal.')
