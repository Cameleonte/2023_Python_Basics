group_number = int(input())

Musala_trackers = 0
Mont_blanc_trackers = 0
Kilimanjaro_trackers = 0
K2_trackers = 0
Everest_trackers = 0

for num in range(group_number):
    current_group = int(input())
    if current_group <= 5:
        Musala_trackers += current_group
    elif current_group <= 12:
        Mont_blanc_trackers += current_group
    elif current_group <= 25:
        Kilimanjaro_trackers += current_group
    elif current_group <= 40:
        K2_trackers += current_group
    else:
        Everest_trackers += current_group

tot_trackers = Musala_trackers + \
               Mont_blanc_trackers + \
               Kilimanjaro_trackers + \
               K2_trackers + \
               Everest_trackers
percent_Musala = Musala_trackers / tot_trackers * 100
percent_Mont_blanc = Mont_blanc_trackers / tot_trackers * 100
percent_Kilimanjaro = Kilimanjaro_trackers / tot_trackers * 100
percent_K2 = K2_trackers / tot_trackers * 100
percent_Everest = Everest_trackers / tot_trackers * 100

print(f'{percent_Musala:.2f}%')
print(f'{percent_Mont_blanc:.2f}%')
print(f'{percent_Kilimanjaro:.2f}%')
print(f'{percent_K2:.2f}%')
print(f'{percent_Everest:.2f}%')
