from math import floor
from math import ceil

wine_yard = int(input())
kg_grape_from1 = float(input())
lt_wine_needed = int(input())
workers = int(input())

produced_grape = wine_yard * kg_grape_from1
grape_for_wine = produced_grape * 0.4
produced_wine = (grape_for_wine / 2.5)
wine_left = abs(produced_wine - lt_wine_needed)

if lt_wine_needed <= produced_wine:
    rounded_produced_wine = floor(produced_wine)
    rounded_wine_left = ceil(wine_left)
    lt_for_worker = ceil(wine_left / workers)
    print(f'Good harvest this year! Total wine: {rounded_produced_wine} liters.')
    print(f'{rounded_wine_left} liters left -> {lt_for_worker} liters per person.')
else:
    rounded_wine_left = floor(wine_left)
    print(f'It will be a tough winter! More {rounded_wine_left} liters wine needed.')
