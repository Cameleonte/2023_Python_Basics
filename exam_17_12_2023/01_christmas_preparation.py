paper_roll = int(input())
cloth_roll = int(input())
glue = float(input())
percent_discount = int(input())

paper_price = paper_roll * 5.8
cloth_price = cloth_roll * 7.2
glue_price = glue * 1.2
tot_sum = paper_price + cloth_price + glue_price
discount = tot_sum * percent_discount / 100
final_sum = tot_sum - discount

print(f'{final_sum:.3f}')
