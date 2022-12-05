print(f"{'Kilogram':<10}{'Pounds':>10}")
for kilograms in range(1, 199, 2):
    pounds = kilograms * 2.2
    print(f"{kilograms:<10}{round(pounds, 1):>10}")