kid_tickets = 0
standard_tickets = 0
student_tickets = 0
movie_name = input()
while movie_name != 'Finish':
    hall_tot_seats = int(input())
    tot_tickets_bought = 0
    for seat in range(1, hall_tot_seats + 1):
        ticket = input()
        if ticket == 'End':
            break
        elif ticket == 'student':
            student_tickets += 1
        elif ticket == 'standard':
            standard_tickets += 1
        elif ticket == 'kid':
            kid_tickets += 1
        tot_tickets_bought += 1
    percentage_hall_fullness = tot_tickets_bought / hall_tot_seats * 100
    print(f'{movie_name} - {percentage_hall_fullness:.2f}% full.')
    movie_name = input()
tot_tickets = kid_tickets + standard_tickets + student_tickets
student_tickets_percent = student_tickets / tot_tickets * 100
standard_tickets_percent = standard_tickets / tot_tickets * 100
kids_tickets_percent = kid_tickets / tot_tickets * 100

print(f'Total tickets: {tot_tickets}')
print(f'{student_tickets_percent:.2f}% student tickets.')
print(f'{standard_tickets_percent:.2f}% standard tickets.')
print(f'{kids_tickets_percent:.2f}% kids tickets.')
