stadium_capacity = int(input())
tot_fans = int(input())

fans_A = 0
fans_B = 0
fans_V = 0
fans_G = 0

for fan in range(1, tot_fans + 1):
    sector = input()
    if sector == 'A':
        fans_A += 1
    elif sector == 'B':
        fans_B += 1
    elif sector == 'V':
        fans_V += 1
    elif sector == 'G':
        fans_G += 1
percent_sec_A = fans_A / tot_fans * 100
percent_sec_B = fans_B / tot_fans * 100
percent_sec_V = fans_V / tot_fans * 100
percent_sec_G = fans_G / tot_fans * 100
percent_tot_fans = tot_fans / stadium_capacity * 100
print(f'{percent_sec_A:.2f}%')
print(f'{percent_sec_B:.2f}%')
print(f'{percent_sec_V:.2f}%')
print(f'{percent_sec_G:.2f}%')
print(f'{percent_tot_fans:.2f}%')

