chicken = int(input())
fish = int(input())
vegan = int(input())

sum_menu = chicken * 10.35 + fish * 12.40 + vegan * 8.15
dessert_price = sum_menu * 0.2
delivery = 2.50
tot_sum = sum_menu + dessert_price + delivery

print(tot_sum)
