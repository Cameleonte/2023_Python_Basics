hours = int(input())
minutes = int(input())

tot_minutes = hours * 60 + minutes + 15
tot_hours = tot_minutes // 60
all_minutes = tot_minutes % 60

if tot_hours > 23:
    tot_hours = 0

print(f'{tot_hours}:{all_minutes:02d}')
