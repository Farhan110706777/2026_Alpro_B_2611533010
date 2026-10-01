# Buat file dengan nama nested_for2_NIM.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh : ulang_3010
# Program ini menggunakan fungsi input ()

batas_3010 = int(input("Masukkan nilai batas: "))
for i_3010 in range(1, batas_3010 + 1):
    for j_3010 in range(1, i_3010 + 1):
        print("*", end="")
    print() # pindah ke baris berikutnya
