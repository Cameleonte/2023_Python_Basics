nylon = int(input())
paint = int(input())
razr = int(input())
hour_workers = int(input())

sum_nylon = (nylon + 2) * 1.5
sum_paint = (paint*1.1) * 14.5
sum_razr = razr * 5

sum_mat = sum_nylon + sum_paint + sum_razr + 0.40
sum_workers = (sum_mat * 0.3) * hour_workers
tot_sum = sum_mat + sum_workers

print(tot_sum)
