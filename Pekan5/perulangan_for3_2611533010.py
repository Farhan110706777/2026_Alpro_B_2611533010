# Buat file dengan nama perulangan_for3_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_3010
# Program ini menggunakan fungsi input()

ulang_3010 = int(input("Masukkan jumlah perulangan: "))

jumlah_3010 = 0
for i_3010 in range(1, ulang_3010 + 1):
    print(i_3010, end=" ")
    jumlah_3010 = jumlah_3010 + i_3010

    if i_3010 < ulang_3010:
        print("+ ", end="")
    else:
        print("= ", jumlah_3010, end="")

print()
print("Jumlah =", jumlah_3010)