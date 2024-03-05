poor_grades_count = int(input())

counter = 0
grades_sum = 0
failed = 0
last_problem_name = ''
too_many_poor_grades = False
problem_name = input()

while problem_name != 'Enough':
    vote = int(input())
    if vote <= 4:
        failed += 1
        if failed == poor_grades_count:
            too_many_poor_grades = True
            break
    grades_sum += vote
    counter += 1
    last_problem_name = problem_name
    problem_name = input()
if too_many_poor_grades:
    print(f'You need a break, {failed} poor grades.')
else:
    average_grade = grades_sum / counter
    print(f'Average score: {average_grade:.2f}')
    print(f'Number of problems: {counter}')
    print(f'Last problem: {last_problem_name}')
