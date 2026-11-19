menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []

# Baca data dengan nested loop dan simpan tiap baris sebagai list baru
for day in range(1, number_of_days + 1):
    row = []
    for menu in menus:
        portion = int(input(f"Day {day}, {menu}: "))
        row.append(portion)
    sales.append(row)

# Traversal per baris: total porsi setiap hari
print("Total per day:")
for day_idx in range(len(sales)):
    day_total = 0
    for menu_idx in range(len(sales[day_idx])):
        day_total += sales[day_idx][menu_idx]
    print(f"Day {day_idx + 1}: {day_total}")

# Traversal per kolom: total porsi setiap menu dalam bentuk list of tuple
menu_totals = []
for menu_idx in range(len(menus)):
    menu_total = 0
    for day_idx in range(len(sales)):
        menu_total += sales[day_idx][menu_idx]
    menu_totals.append((menus[menu_idx], menu_total))

print(f"Total per menu: {menu_totals}")

# Cari menu terlaris (jika seri, ambil yang muncul lebih dulu)
best_name = menu_totals[0][0]
best_total = menu_totals[0][1]

for name, total in menu_totals:
    if total > best_total:
        best_total = total
        best_name = name

print(f"Best seller: {best_name} ({best_total})")