jury_members = int(input())

total_grade = 0
presentation_counter = 0
presentation_title = input()

while presentation_title != 'Finish':
    average_presentation_grade = 0
    sum_grades = 0
    for grade in range(1, jury_members + 1):
        presentation_grade = float(input())
        sum_grades += presentation_grade
    average_presentation_grade = sum_grades / jury_members
    print(f'{presentation_title} - {average_presentation_grade:.2f}.')
    presentation_title = input()
    presentation_counter += 1
    total_grade += average_presentation_grade
final_average_grade = total_grade / presentation_counter
print(f'Student\'s final assessment is {final_average_grade:.2f}.')
