width = int(input())
length = int(input())

max_pieces = length * width
tot_pieces = 0

while max_pieces >= tot_pieces:
    text = input()
    if text == 'STOP':
        left_pieces = max_pieces - tot_pieces
        print(f'{left_pieces} pieces are left.')
        break
    current_pieces = int(text)
    tot_pieces += current_pieces
    if tot_pieces > max_pieces:
        difference = abs(tot_pieces - max_pieces)
        print(f'No more cake left! You need {difference} pieces more.')
        break
