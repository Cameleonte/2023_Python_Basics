pens_count = int(input())
markers_count = int(input())
detergent_count = int(input())
disc_percent = int(input())

price_pen = pens_count * 5.80
price_markers = markers_count * 7.20
price_detergent = detergent_count * 1.20

tot_price = price_pen + price_markers + price_detergent
disc_price = tot_price * (disc_percent / 100)
final_price = tot_price - disc_price

print(final_price)