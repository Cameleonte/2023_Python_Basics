load_number = int(input())

tot_ton_load = 0
percent_load_bus = 0
percent_load_truck = 0
percent_load_train = 0
mid_price_load = 0
bus_price_load = 0
truck_price_load = 0
train_price_load = 0
bus_ton_load = 0
truck_ton_load = 0
train_ton_load = 0

for load in range(1, load_number + 1):
    tons = int(input())
    tot_ton_load += tons
    if tons <= 3:
        bus_price_load += tons * 200
        bus_ton_load += tons
    elif tons <= 11:
        truck_price_load += tons * 175
        truck_ton_load += tons
    else:
        train_price_load += tons * 120
        train_ton_load += tons
mid_price_load = (bus_price_load + truck_price_load + train_price_load) / tot_ton_load
percent_load_bus = bus_ton_load / tot_ton_load * 100
percent_load_truck = truck_ton_load / tot_ton_load * 100
percent_load_train = train_ton_load / tot_ton_load * 100
print(f'{mid_price_load:.2f}')
print(f'{percent_load_bus:.2f}%')
print(f'{percent_load_truck:.2f}%')
print(f'{percent_load_train:.2f}%')
