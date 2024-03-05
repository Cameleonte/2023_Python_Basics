deposit_amount = float(input())
months = int(input())
annual_rate = float(input())

interest_per_year = deposit_amount * (annual_rate/100)
interest_per_month = interest_per_year / 12

final_sum: float = deposit_amount + months * interest_per_month

print(final_sum)
