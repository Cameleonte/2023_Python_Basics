from math import ceil
from math import floor

days_gone = int(input())
food_left = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input())

food_eaten = dog_food_per_day * days_gone + cat_food_per_day * days_gone + (turtle_food_per_day * days_gone) / 1000
food_rest = abs(food_left - food_eaten)

if food_left >= food_eaten:
    rounded_food_rest = floor(food_rest)
    print(f'{rounded_food_rest} kilos of food left.')
else:
    rounded_food_rest = ceil(food_rest)
    print(f'{rounded_food_rest} more kilos of food are needed.')
