# Buat file dengan nama Boolean_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: nilai_1234
# Deklarasi variabel dengan tipe data Boolean
is_lulus_3010 = True 
is_cumlaude_3010 = True

# Menggunakan Boolean
nilai_3010 = 85
batas_lulus_3010 = 75

# Menentukan nilai Boolean dari kondisi
status_kelulusan_3010 = nilai_3010 >= batas_lulus_3010 # Hasilnya akan True

print("=== Check Kelulusan ===")
print("Nilai:", nilai_3010)
print("Apakah Lulus:", status_kelulusan_3010)
if is_lulus_3010 and is_cumlaude_3010:

    print("Selamat, Anda lulus dengan predikat Cum Laude!")