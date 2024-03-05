length = int(input())
width = int(input())
high = int(input())

space_m_cubic = length * width * high
m_cubic_occupied = 0

while space_m_cubic >= m_cubic_occupied:
    text = input()
    if text == 'Done':
        if space_m_cubic > m_cubic_occupied:
            m_cubic_left = space_m_cubic - m_cubic_occupied
            print(f'{m_cubic_left} Cubic meters left.')
            break
    cartons_qty = int(text)
    m_cubic_occupied += cartons_qty
if space_m_cubic < m_cubic_occupied:
    difference = abs(space_m_cubic - m_cubic_occupied)
    print(f'No more free space! You need {difference} Cubic meters more.')
