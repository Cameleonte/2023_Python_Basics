from math import floor
current_word = input()
sum_symbols = 0
for letter in current_word:
    sum_symbols += ord(letter)

sum_symbols /= (len(current_word))
sum_symbols = floor(sum_symbols)
print(sum_symbols)
