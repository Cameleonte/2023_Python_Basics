first_time = int(input())
second_time = int(input())
third_time = int(input())

tot_seconds = first_time + second_time + third_time
minutes = tot_seconds // 60
seconds = tot_seconds % 60

print(f'{minutes}:{seconds:02d}')
