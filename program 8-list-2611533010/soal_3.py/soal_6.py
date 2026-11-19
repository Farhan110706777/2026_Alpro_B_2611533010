LAST_DIGIT = 0  # ubah ke digit terakhir NIM Anda (contoh: 0 untuk NIM akhiran 0)
daily_limit = 30000 + LAST_DIGIT * 1000
expenses = []

# Baca 7 pengeluaran
for i in range(1, 8):
    amount = int(input(f"Day {i}: "))
    expenses.append(amount)

# Hitung total, pengeluaran tertinggi, dan jumlah hari di atas batas
total = 0
highest_val = expenses[0]
highest_day = 1
days_above_limit = 0

for idx in range(len(expenses)):
    val = expenses[idx]
    total += val

    if val > highest_val:
        highest_val = val
        highest_day = idx + 1

    if val > daily_limit:
        days_above_limit += 1

average = total / len(expenses)

# Cetak 5 baris hasil
print(f"Daily limit: {daily_limit}")
print(f"Total: {total}")
print(f"Average: {average:.1f}")
print(f"Highest: day {highest_day} ({highest_val})")
print(f"Days above limit: {days_above_limit}")