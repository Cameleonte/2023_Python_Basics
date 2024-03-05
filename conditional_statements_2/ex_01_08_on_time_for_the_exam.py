exam_hour = int(input())
exam_min = int(input())
arrive_hour = int(input())
arrive_min = int(input())

time_exam = exam_hour * 60 + exam_min
time_arrive = arrive_hour * 60 + arrive_min

if time_arrive < time_exam - 30:
    print('Early')
elif time_exam - 30 <= time_arrive <= time_exam:
    print('On time')
elif time_arrive > time_exam:
    print('Late')

difference = abs(time_arrive - time_exam)
hour = difference // 60
minutes = difference % 60

if time_arrive <= time_exam - 60:
    print(f'{hour}:{minutes:02d} hours before the start')
elif time_exam - 60 < time_arrive < time_exam:
    print(f'{minutes} minutes before the start')
elif time_exam < time_arrive < time_exam + 60:
    print(f'{minutes} minutes after the start')
elif time_arrive >= time_exam + 60:
    print(f'{hour}:{minutes:02d} hours after the start')
