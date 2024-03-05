period = int(input())

doctors = 7
treated_patients = 0
untreated_patients = 0

for days in range(1, period + 1):
    patients_number = int(input())
    if days % 3 == 0 and untreated_patients > treated_patients:
        doctors += 1
    if patients_number < doctors:
        treated_patients += patients_number
    else:
        treated_patients += doctors
        untreated_patients += patients_number - doctors

print(f'Treated patients: {treated_patients}.')
print(f'Untreated patients: {untreated_patients}.')
