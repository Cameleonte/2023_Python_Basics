students = int(input())

average_vote = 0
votes_to_3 = 0
votes_to_4 = 0
votes_to_5 = 0
votes_to_6 = 0
sum_votes = 0

for num in range(1, students + 1):
    grade = float(input())
    if 2 <= grade < 3:
        votes_to_3 += 1
    elif grade < 4:
        votes_to_4 += 1
    elif grade < 5:
        votes_to_5 += 1
    elif grade <= 6:
        votes_to_6 += 1
    sum_votes += grade
percent_votes_to_3 = votes_to_3 / students * 100
percent_votes_to_4 = votes_to_4 / students * 100
percent_votes_to_5 = votes_to_5 / students * 100
percent_votes_to_6 = votes_to_6 / students * 100
average_vote = sum_votes / students
print(f'Top students: {percent_votes_to_6:.2f}%')
print(f'Between 4.00 and 4.99: {percent_votes_to_5:.2f}%')
print(f'Between 3.00 and 3.99: {percent_votes_to_4:.2f}%')
print(f'Fail: {percent_votes_to_3:.2f}%')
print(f'Average: {average_vote:.2f}')
