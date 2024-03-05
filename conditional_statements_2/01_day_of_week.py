day_of_week = int(input())
data_input = 'Error'

if day_of_week == 1:
    data_input = 'Monday'
elif day_of_week == 2:
    data_input = 'Tuesday'
elif day_of_week == 3:
    data_input = 'Wednesday'
elif day_of_week == 4:
    data_input = 'Thursday'
elif day_of_week == 5:
    data_input = 'Friday'
elif day_of_week == 6:
    data_input = 'Saturday'
elif day_of_week == 7:
    data_input = 'Sunday'

print(data_input)
