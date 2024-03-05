open_tabs = int(input())
salary = float(input())

charge = 0

for site in range(open_tabs):
    open_site = input()
    if open_site == 'Facebook':
        charge += 150
    elif open_site == 'Instagram':
        charge += 100
    elif open_site == 'Reddit':
        charge += 50
    if charge >= salary:
        break
if charge < salary:
    difference = salary - charge
    print(f'{difference:.0f}')
else:
    print('You have lost your salary.')

'''
website_name = input()
    if website_name == "Facebook":
        salary -= 150
    elif website_name == "Instagram":
        salary -= 100
    elif website_name == "Reddit":
        salary -= 50
    if salary <= 0:
        break
if salary > 0:
    print(salary)
else:
    print("You have lost your salary.")
'''