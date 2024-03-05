floors = int(input())
rooms = int(input())

for i in reversed(range(1, floors + 1)):
    apartments = 'O' if i % 2 == 0 else 'A'
    if i == floors:
        apartments = 'L'
    for j in range(rooms):
        print(f'{apartments}{i}{j}', end=' ')
    print()