day_of_week = input()
data_output = 'Error'

if day_of_week == 'Monday':
    data_output = 'Working day'
elif day_of_week == 'Tuesday':
    data_output = 'Working day'
elif day_of_week == 'Wednesday':
    data_output = 'Working day'
elif day_of_week == 'Thursday':
    data_output = 'Working day'
elif day_of_week == 'Friday':
    data_output = 'Working day'
elif day_of_week == 'Saturday':
    data_output = 'Weekend'
elif day_of_week == 'Sunday':
    data_output = 'Weekend'

print(data_output)
