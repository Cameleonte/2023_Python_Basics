number = int(input())

tot_sum = 0
tot_sum1 = 0

for num in range(number):
    current_number = int(input())
    tot_sum += current_number
for num1 in range(number):
    current_number1 = int(input())
    tot_sum1 += current_number1
if tot_sum == tot_sum1:
    print(f'Yes, sum = {tot_sum}')
else:
    difference = abs(tot_sum - tot_sum1)
    print(f'No, diff = {difference}')
