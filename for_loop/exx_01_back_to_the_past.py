heritage = float(input())
year_to_reach = int(input())

ivan_years = 18

for year in range(1800, year_to_reach + 1):
    if year % 2 == 0:
        heritage -= 12000
    else:
        heritage -= 12000 + 50 * ivan_years
    ivan_years += 1

difference = abs(heritage)
if heritage >= 0:
    print(f'Yes! He will live a carefree life and will have {difference:.2f} dollars left.')
else:
    print(f'He will need {difference:.2f} dollars to survive.')
