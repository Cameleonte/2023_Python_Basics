student_name = input()

votes_count = 0
average_vote = 0
votes_sum = 0
bad_votes_count = 0

while votes_count < 12:
    annual_vote = float(input())
    if annual_vote >= 4:
        votes_count += 1
        votes_sum += annual_vote
        average_vote = votes_sum / votes_count
        continue

    if annual_vote < 4:
        bad_votes_count += 1
        if bad_votes_count < 2:
            continue
        else:
            print(f'{student_name} has been excluded at {votes_count + 1} grade')
            break
if votes_count == 12:
    print(f'{student_name} graduated. Average grade: {average_vote:.2f}')