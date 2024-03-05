from math import floor

length = float(input())
width = float(input())

real_width = width - 1
seats_in_width = floor(real_width / 0.7)
seats_in_length = floor(length / 1.2)
tot_seats = seats_in_width * seats_in_length - 3

print(tot_seats)
