# Buat file dengan nama multi_if2_NIM.py
# Buat program untuk kondisional if
# Buat variabel ditambah 4 digit nim terakhir contoh : total_belanja_3010
# Program ini menggunakan fungsi input ()
# Program Menghitung Diskon Belanja

# Input dari user
total_belanja_3010 = float(input("Input total belanja (Rp): "))

# Input status member (mengecek apakah user mengetik 'y' atau'ya)
input_member_3010 = input("Apakah Anda Member (y/t): ").strip().lower()
is_member_3010 = input_member_3010 in ["y", "ya"]

# Input status kode promo (mengecek apakah user mengetik 'y' atau'ya)
input_promo_3010 = input("Apakah Kode Promo valid? (y/t): ").strip().lower()
kode_promo_valid_3010 = input_promo_3010 in ["y", "ya"]

total_diskon_persen = 0

# Multi-If terpisah: Setiap kondisi diperiksa secara independen
# Diskon bisa ditumpuk (akumulasi) jika memenuhi beberapa syarat sekaligus

if total_belanja_3010 > 1000000:
    total_diskon_persen += 10  # Diskon belanja besar

if is_member_3010:
    total_diskon_persen += 5  # Diskon member

if kode_promo_valid_3010:
    total_diskon_persen += 15  # Diskon voucher

# Menghitung nominal diskon dan total bayar
nominal_diskon_3010 = total_belanja_3010 * (total_diskon_persen / 100)
total_bayar_3010 = total_belanja_3010 - nominal_diskon_3010

# Output hasil 
print("\n--- Rincian Pembayaran ---")
print(f"Total Diskon : {total_diskon_persen}% (Rp {nominal_diskon_3010:,.0f})")
print(f"Total Bayar  : Rp {total_bayar_3010:,.0f}")

print(f"Total diskon yang Anda dapatkan: {total_diskon_persen}%")
# Output: Total diskon yang Anda dapatkan: 30% jika belanja > 1 juta, member, dan kode promo valid valid