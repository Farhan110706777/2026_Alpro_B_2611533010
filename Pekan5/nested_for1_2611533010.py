# Buat file dengan nama nested_for1_NIM.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh : ulang_3010
# Program ini menggunakan fungsi input ()

batas_3010 = int(input("Masukkan nilai batas_3010: "))
for line_3010 in range(1, batas_3010 + 1):
    for j_3010 in range(1, (-1 * line_3010 + batas_3010 + 1)):
        print(".", end=" ")
        print(line_3010)