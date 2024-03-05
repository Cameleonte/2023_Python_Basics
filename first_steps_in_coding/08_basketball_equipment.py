year_tax = int(input())

sneakers_pr = year_tax * 0.6
suit_pr = sneakers_pr * 0.8
ball_pr = suit_pr * 0.25
accessories_pr = ball_pr * 0.2

tot_pr = year_tax + sneakers_pr + suit_pr + ball_pr + accessories_pr

print(tot_pr)
