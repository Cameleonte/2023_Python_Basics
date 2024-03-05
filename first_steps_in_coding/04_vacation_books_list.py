book_pages = int(input())
pages_per_hour = int(input())
days_to_read = int(input())

book_time = book_pages // pages_per_hour
hours_per_day = book_time // days_to_read

print(hours_per_day)
