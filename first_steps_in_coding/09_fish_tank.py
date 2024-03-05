length = int(input())
width = int(input())
height = int(input())
percent = float(input())

vol_aquarium = length * width * height
vol_in_lt = vol_aquarium * 0.001
occ_vol = vol_in_lt * (percent / 100)
lt_needed = vol_in_lt - occ_vol

print(lt_needed)