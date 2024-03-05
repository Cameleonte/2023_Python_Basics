temperature = int(input())
part_of_day = input()
outfit = ''
shoes = ''

if (part_of_day == 'Afternoon' or part_of_day == 'Evening') and 10 <= temperature <= 18:
    outfit = 'Shirt'
    shoes = 'Moccasins'
elif part_of_day == 'Morning' and 10 <= temperature <= 18:
    outfit = 'Sweatshirt'
    shoes = 'Sneakers'
elif (part_of_day == 'Morning' or part_of_day == 'Evening') and 18 < temperature <= 24:
    outfit = 'Shirt'
    shoes = 'Moccasins'
elif part_of_day == 'Afternoon' and 18 < temperature <= 24:
    outfit = 'T-Shirt'
    shoes = 'Sandals'
elif part_of_day == 'Morning' and temperature >= 25:
    outfit = 'T-Shirt'
    shoes = 'Sandals'
elif part_of_day == 'Afternoon' and temperature >= 25:
    outfit = 'Swim Suit'
    shoes = 'Barefoot'
elif part_of_day == 'Evening' and temperature >= 25:
    outfit = 'Shirt'
    shoes = 'Moccasins'

print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")
