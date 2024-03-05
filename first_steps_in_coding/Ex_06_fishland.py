mackerel_price = float(input())
sprinkle_price = float(input())
bonito_kg = float(input())
safrid_kg = float(input())
clams_kg = int(input())

bonito_price = mackerel_price * 1.6 * bonito_kg
safrid_price = sprinkle_price * 1.8 * safrid_kg
clams_price = clams_kg * 7.50
tot_price = bonito_price + safrid_price + clams_price

#print('%.2f' % tot_price)
print(f'{tot_price:.2f}')
