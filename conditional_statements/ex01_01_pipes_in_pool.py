pool_volume = int(input())
debit1 = int(input())
debit2 = int(input())
missing_hours = float(input())

pool_volume_h = debit1 * missing_hours + debit2 * missing_hours
percent_vol = pool_volume_h * 100 / pool_volume
vol_debit1 = debit1 * missing_hours
vol_debit2 = debit2 * missing_hours
percent_debit1 = vol_debit1 * 100 / pool_volume_h
percent_debit2 = vol_debit2 * 100 / pool_volume_h

if pool_volume_h <= pool_volume:
    print(f'The pool is {percent_vol}% full. Pipe 1: {percent_debit1:.2f}%. Pipe 2: {percent_debit2:.2f}%.')
else:
    lt_above = vol_debit1 + vol_debit2 - pool_volume
    print(f'For {missing_hours} hours the pool overflows with {lt_above} liters.')
