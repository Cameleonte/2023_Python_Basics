width_x = float(input())
length_y = float(input())
roof_height_h = float(input())

area_front_end = 2 * width_x ** 2 - 1.2 * 2.0
area_sides = 2 * width_x * length_y - 2 * 1.5 * 1.5
tot_area_roof = 2 * width_x * length_y + 2 * width_x * roof_height_h / 2
tot_side_area = area_front_end + area_sides
quantity_green_paint = tot_side_area / 3.40
quantity_red_paint = tot_area_roof / 4.30

print('%.2f' % quantity_green_paint)
print('%.2f' % quantity_red_paint)
