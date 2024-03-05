excursion_price = float(input())
puzzle_count = int(input())
toy_count = int(input())
bears_count = int(input())
minions_count = int(input())
truck_count = int(input())

total_price = puzzle_count * 2.6 + toy_count * 3 + bears_count * 4.1 + minions_count * 8.2 + truck_count * 2

if puzzle_count + toy_count + bears_count + minions_count + truck_count >= 50:
    total_price = total_price * 0.75

total_price *= 0.9
rest = abs(total_price - excursion_price)

if total_price >= excursion_price:
    print(f"Yes! {rest:.2f} lv left.")
else:
    print(f'Not enough money! {rest:.2f} lv needed.')
