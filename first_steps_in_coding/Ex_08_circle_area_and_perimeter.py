from math import pi

radius = float(input())

perimeter = 2 * radius * pi
area = pi * radius * radius

#print("%.2f" % area)
#print("%.2f" % perimeter)
print(f'{area:.2f}')
print(f'{perimeter:.2f}')
