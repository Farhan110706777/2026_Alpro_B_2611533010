# Buat file dengan nama perulanga_for2_NIM.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh : ulang_3010
# Program ini menggunakan fungsi input ()

ulang_3010 = int(input("masukkan jumlah perulangan: "))
print("Perulangan ke-0 sampai ke-", ulang_3010-1)
for i in range(ulang_3010):
    print(i, end=" ")
print ()
print("Perulangan ke-1 sampai ke-", ulang_3010)
for i_3010 in range(1, ulang_3010 + 1):
    print(i_3010, end=" ")