projection_type = input()
rows = int(input())
columns = int(input())
capacity = rows * columns
tot_income = 0

if projection_type == 'Premiere':
    tot_income = capacity * 12
elif projection_type == 'Normal':
    tot_income = capacity * 7.5
elif projection_type == 'Discount':
    tot_income = capacity * 5

print(f'{tot_income:.2f} leva')
