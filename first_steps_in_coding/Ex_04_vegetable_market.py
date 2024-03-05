price_per_kg_vegetables_lv = float(input())
price_per_kg_fruit_lv = float(input())
tot_kg_vegetables = float(input())
tot_kg_fruit = float(input())

price_vegetables_lv = price_per_kg_vegetables_lv * tot_kg_vegetables
price_fruit_lv = price_per_kg_fruit_lv * tot_kg_fruit
tot_price_lv = price_vegetables_lv + price_fruit_lv
tot_price_euro = tot_price_lv / 1.94

#print('%.2f' % tot_price_euro)
print(f'{tot_price_euro:.2f}')
