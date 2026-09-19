# Tugas3_2611533010.py
# Sistem Simulasi Transaksi dan Validasi Akses Toko

print("=== SISTEM TRANSAKSI TOKO ===\n")

# Input Data Pelanggan
nama_3010 = input("Masukkan Nama Pelanggan : ")
status_3010 = input("Masukkan Status Pelanggan (member/nonmember) : ").lower()
total_belanja_3010 = int(input("Masukkan Total Belanja : "))
jumlah_barang_3010 = int(input("Masukkan Jumlah Barang : "))
kode_promo_input_3010 = input("Masukkan Kode Promo : ")

# Operator Keanggotaan
daftar_promo_3010 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]
promo_tersedia_3010 = kode_promo_input_3010 in daftar_promo_3010
promo_tidak_valid_3010 = kode_promo_input_3010 not in daftar_promo_3010

# Operator Perbandingan & Logika
syarat_belanja_3010 = total_belanja_3010 >= 200000
syarat_barang_3010 = jumlah_barang_3010 >= 3
is_member_3010 = status_3010 == "member"

# Logika Penggabungan (and)
dapat_diskon_3010 = is_member_3010 and syarat_belanja_3010
dapat_promo_3010 = promo_tersedia_3010 and syarat_barang_3010

# Operator Identitas
promo_ref_3010 = daftar_promo_3010
promo_copy_3010 = daftar_promo_3010.copy()

# Membuktikan identitas objek
is_same_object_3010 = promo_ref_3010 is daftar_promo_3010
is_diff_object_3010 = promo_copy_3010 is not daftar_promo_3010

# Operator Aritmatika & Penugasan
besaran_diskon_3010 = 0
if dapat_diskon_3010:
    besaran_diskon_3010 = total_belanja_3010 * 10 // 100 # Diskon 10%

# Assignment
total_pembayaran_3010 = total_belanja_3010
total_pembayaran_3010 -= besaran_diskon_3010 # Augmented assignment pengurangan

# Aritmatika lanjutan
rata_rata_harga_3010 = total_belanja_3010 // jumlah_barang_3010
sisa_bagi_3010 = total_belanja_3010 % jumlah_barang_3010

# 6. Operator Bitwise
# 0001 (1) = Member | 0010 (2) = Belanja >= 200k | 0100 (4) = Barang >= 3 | 1000 (8) = Promo
status_code_3010 = 0
if is_member_3010: status_code_3010 |= 1
if syarat_belanja_3010: status_code_3010 |= 2
if syarat_barang_3010: status_code_3010 |= 4
if promo_tersedia_3010: status_code_3010 |= 8

cek_member_bitwise_3010 = status_code_3010 & 1
cek_promo_bitwise_3010 = status_code_3010 & 8

# Perbandingan Status (XOR) dan Shift
kode_referensi_3010 = 11 # 1011 Biner
hasil_xor_3010 = status_code_3010 ^ kode_referensi_3010
shift_kiri_3010 = status_code_3010 << 1

# === OUTPUT PROGRAM ===
print("\n=== DATA TRANSAKSI ===")
print(f"Nama Pelanggan       : {nama_3010}")
print(f"Status Pelanggan     : {status_3010}")
print(f"Total Belanja        : Rp{total_belanja_3010}")
print(f"Jumlah Barang        : {jumlah_barang_3010}")
print(f"Kode Promo           : {kode_promo_input_3010}")

print("\n=== HASIL VALIDASI ===")
print(f"Belanja >= Rp200000  : {syarat_belanja_3010}")
print(f"Jumlah Barang >= 3   : {syarat_barang_3010}")
print(f"Status Member        : {is_member_3010}")
print(f"Kode Promo Tersedia  : {promo_tersedia_3010}")
print(f"Mendapatkan Diskon   : {dapat_diskon_3010}")
print(f"Mendapatkan Promo    : {dapat_promo_3010}")

print("\n=== HASIL PERHITUNGAN ===")
print(f"Diskon               : Rp{besaran_diskon_3010}")
print(f"Total Pembayaran     : Rp{total_pembayaran_3010}")
print(f"Rata-rata Harga Barang : Rp{rata_rata_harga_3010}")
print(f"Sisa Bagi (Modulus)  : Rp{sisa_bagi_3010}")

print("\n=== HAK AKSES PELANGGAN ===")
print(f"Kode Hak Akses       : {format(status_code_3010, '04b')}")
print(f"Member Access        : {bool(cek_member_bitwise_3010)}")
print(f"Promo Access         : {bool(cek_promo_bitwise_3010)}")

print("\n=== OPERASI BITWISE ===")
print("=== Kode Status Transaksi ===")
print(f"Kode Biner   : {format(status_code_3010, '04b')}")
print(f"Kode Desimal : {status_code_3010}")

print("\n=== Pemeriksaan Status ===")
print("Cek Member")
print(f"{format(status_code_3010, '04b')} & 0001")
print(f"Hasil Biner   : {format(cek_member_bitwise_3010, '04b')}")
print(f"Hasil Desimal : {cek_member_bitwise_3010}")

print("\nCek Promo")
print(f"{format(status_code_3010, '04b')} & 1000")
print(f"Hasil Biner   : {format(cek_promo_bitwise_3010, '04b')}")
print(f"Hasil Desimal : {cek_promo_bitwise_3010}")

print("\n=== Perbandingan Status ===")
print(f"Kode Transaksi : {format(status_code_3010, '04b')}")
print(f"Kode Referensi : {format(kode_referensi_3010, '04b')}")
print(f"{format(status_code_3010, '04b')} ^ {format(kode_referensi_3010, '04b')}")
print(f"Hasil Biner   : {format(hasil_xor_3010, '04b')}")
print(f"Hasil Desimal : {hasil_xor_3010}")

print("\n=== Shift ===")
print(f"{format(status_code_3010, '04b')} << 1")
print(f"Hasil Biner   : {format(shift_kiri_3010, '05b')}")
print(f"Hasil Desimal : {shift_kiri_3010}")
print("\n=== SELESAI ===")