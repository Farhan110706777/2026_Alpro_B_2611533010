from typing import Final

# 1. Penerapan Konstanta
BATAS_LULUS: Final = 75.0

# Header Program
print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")

# 2. Input Data & Type Casting
nama_3010 = input("Masukkan Nama Mahasiswa   : ")
jk_3010 = input("Masukkan Jenis Kelamin (L/P): ")
umur_3010 = int(input("Masukkan Umur            : "))
skor_3010 = float(input("Masukkan Skor Tes Awal   : "))

# Alamat multiline
alamat_3010 = """Jl. Muhammad Yunus No 4,
Kecamatan Kuranji,
Kota Padang"""

# Token Sinyal (Complex)
token_3010 = 100 + 3j

# Evaluasi Status Kelulusan (Bool)
status_lulus_3010 = skor_3010 >= BATAS_LULUS

# 3. Output Data & Tipe Data
print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")
print(f"Nama Mahasiswa : {nama_3010} | Tipe: {type(nama_3010)}")
print(f"Jenis Kelamin  : {jk_3010} | Tipe: {type(jk_3010)}")
print(f"Alamat Domisili:\n{alamat_3010}\n| Tipe: {type(alamat_3010)}")
print(f"Umur           : {umur_3010} tahun | Tipe: {type(umur_3010)}")
print(f"Skor Tes Awal  : {skor_3010} | Tipe: {type(skor_3010)}")
print(f"ID Token Sinyal: {token_3010} | Tipe: {type(token_3010)}")

print("\n=== STATUS KELULUSAN PRAKTIKUM ===")
print(f"Batas Minimum Nilai: {BATAS_LULUS}")
print(f"Apakah Dinyatakan Lulus?: {status_lulus_3010} | Tipe: {type(status_lulus_3010)}")