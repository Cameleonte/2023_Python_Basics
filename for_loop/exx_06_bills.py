months = int(input())

tot_others_sum = 0
tot_el_sum = 0

for one_month in range (1, months + 1):
    el_bill = float(input())
    tot_el_sum += el_bill
    tot_others_sum += 15 + 20 + el_bill + 0.2 * (15 + 20 + el_bill)
tot_water_sum = 20 * months
tot_internet_sum = 15 * months
average_sum = (tot_el_sum + tot_water_sum + tot_internet_sum + tot_others_sum) / months
print(f'Electricity: {tot_el_sum:.2f} lv')
print(f'Water: {tot_water_sum:.2f} lv')
print(f'Internet: {tot_internet_sum:.2f} lv')
print(f'Other: {tot_others_sum:.2f} lv')
print(f'Average: {average_sum:.2f} lv')
