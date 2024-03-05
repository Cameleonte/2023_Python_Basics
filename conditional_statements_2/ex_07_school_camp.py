season = input()
group_type = input()
students = int(input())
nights = int(input())

sport_type = ''
night_cost = 0

if season == 'Winter' and group_type == 'girls':
    sport_type = 'Gymnastics'
    night_cost = 9.6
elif season == 'Winter' and group_type == 'boys':
    sport_type = 'Judo'
    night_cost = 9.6
elif season == 'Winter' and group_type == 'mixed':
    sport_type = 'Ski'
    night_cost = 10
elif season == 'Spring' and group_type == 'girls':
    sport_type = 'Athletics'
    night_cost = 7.2
elif season == 'Spring' and group_type == 'boys':
    sport_type = 'Tennis'
    night_cost = 7.2
elif season == 'Spring' and group_type == 'mixed':
    sport_type = 'Cycling'
    night_cost = 9.5
elif season == 'Summer' and group_type == 'girls':
    sport_type = 'Volleyball'
    night_cost = 15
elif season == 'Summer' and group_type == 'boys':
    sport_type = 'Football'
    night_cost = 15
elif season == 'Summer' and group_type == 'mixed':
    sport_type = 'Swimming'
    night_cost = 20

discount = 0

if students >= 50:
    discount = 0.5
elif 20 <= students < 50:
    discount = 0.15
elif 10 <= students < 20:
    discount = 0.05

tot_cost = night_cost * nights * students * (1 - discount)

print(f'{sport_type} {tot_cost:.2f} lv.')
