from math import floor

record_time = float(input())
distance = float(input())
time_for_meter = float(input())

ivan_time = distance * time_for_meter
delay_time = floor(distance / 15) * 12.5
final_time = ivan_time + delay_time

if final_time < record_time:
    print(f'Yes, he succeeded! The new world record is {final_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {final_time - record_time:.2f} seconds slower.')
