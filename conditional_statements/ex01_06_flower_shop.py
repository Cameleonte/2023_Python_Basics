from math import ceil
from math import floor

magnolias_count = int(input())
hyacinths_count = int(input())
roses_count = int(input())
cactus_count = int(input())
present_price = float(input())

paid = magnolias_count * 3.25 + hyacinths_count * 4 + roses_count * 3.5 + cactus_count * 8
paid_after_taxes = paid * 0.95
money = abs(paid_after_taxes - present_price)

if paid_after_taxes >= present_price:
    x = floor(money)
    print(f'She is left with {x} leva.')
else:
    x = ceil(money)
    print(f'She will have to borrow {x} leva.')
