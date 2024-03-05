juniors_count = int(input())
seniors_count = int(input())
trace_type = input()

participants = juniors_count + seniors_count
is_valid_juniors = True
is_valid_seniors = True
tax_juniors = 0
tax_seniors = 0

if trace_type == 'trail' and is_valid_juniors and is_valid_seniors:
    tax_juniors = 5.5
    tax_seniors = 7
elif trace_type == 'cross-country':
    if is_valid_juniors and is_valid_seniors and participants >= 50:
        tax_juniors = 8 * 0.75
        tax_seniors = 9.5 * 0.75
    elif is_valid_juniors and is_valid_seniors and 0 < participants < 50:
        tax_juniors = 8
        tax_seniors = 9.5
elif trace_type == 'downhill' and is_valid_juniors and is_valid_seniors:
    tax_juniors = 12.25
    tax_seniors = 13.75
elif trace_type == 'road' and is_valid_juniors and is_valid_seniors:
    tax_juniors = 20
    tax_seniors = 21.5

tot_sum = juniors_count * tax_juniors + seniors_count * tax_seniors
expenses = tot_sum * 0.05
donations = tot_sum - expenses

print(f'{donations:.2f}')
