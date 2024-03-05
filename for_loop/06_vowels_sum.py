text = input()
tot_sum = 0

for i in range(0, len(text)):
    if text[i] == 'a':
        tot_sum += 1
    if text[i] == 'e':
        tot_sum += 2
    if text[i] == 'i':
        tot_sum += 3
    if text[i] == 'o':
        tot_sum += 4
    if text[i] == 'u':
        tot_sum += 5
print(tot_sum)
