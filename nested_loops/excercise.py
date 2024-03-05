aim = int(input())

tot_jumps = 0
current_pole_height = 0
failed = False
successes = False
current_jump_height = int(input())

while not failed:
    for attempt in range(1, 3 + 1):
        current_jump = 0
        if successes:
            break
        tot_jumps += 1
        if current_jump > 3:
            failed = True
            print(f'Tihomir failed at {current_pole_height}cm after {tot_jumps} jumps.')
            break
        for current_pole_height in range(aim - 30, aim + 1, 5):
            current_jump += 1
            if current_pole_height > current_jump_height:
                break
            else:
                if current_pole_height >= aim:
                    successes = True
                    break
                current_jump_height = int(input())
    break
if not failed or successes:
    print(f'Tihomir succeeded, he jumped over {current_pole_height}cm after {tot_jumps} jumps.')
