chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
weekend = input()

flowers_qty = chrysanthemums + roses + tulips
flowers_price = 0

if season == 'Spring' or season == 'Summer':
    flowers_price = 2 * chrysanthemums + 4.1 * roses + 2.5 * tulips
    if weekend == 'Y':
        flowers_price = flowers_price * 1.15
    if season == 'Spring' and tulips > 7:
        flowers_price = flowers_price * 0.95
    if flowers_qty > 20:
        flowers_price = flowers_price * 0.8
elif season == 'Autumn' or season == 'Winter':
    flowers_price = 3.75 * chrysanthemums + 4.5 * roses + 4.15 * tulips
    if weekend == 'Y':
        flowers_price = flowers_price * 1.15
    if season == 'Winter' and roses >= 10:
        flowers_price = flowers_price * 0.9
    if flowers_qty > 20:
        flowers_price = flowers_price * 0.8

print(f'{(flowers_price + 2):.2f}')
