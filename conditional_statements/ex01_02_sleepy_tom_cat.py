holidays = int(input())

work_days = 365 - holidays
play_time_work_days = work_days * 63
play_time_rest = holidays * 127
tot_play_time = play_time_work_days + play_time_rest
diff = abs(30000 - tot_play_time)
hours = diff // 60
minutes = diff % 60

if tot_play_time > 30000:
    print('Tom will run away')
    print(f'{hours} hours and {minutes} minutes more for play')
else:
    print('Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less for play')
