number = int(input())

for num in range(0, number + 1, 2):
    step_num = 2 ** num
    print(step_num)
