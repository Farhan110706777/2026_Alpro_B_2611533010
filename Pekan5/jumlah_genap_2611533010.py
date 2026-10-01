# Buat file dengan nama jumlah_3010_genap_NIM.py
# Buat program untuk perulang_3010an for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh : ulang_3010_3010
# Program ini menggunakan fungsi input ()

ulang_3010 = int(input("masukkan nilai batas: "))

jumlah_3010 = 0
for i_3010 in range(1,ulang_3010+1):
    if i_3010 % 2 == 0:
        print(i_3010, end=" ")
        jumlah_3010 = jumlah_3010 + i_3010

        if i_3010 < ulang_3010:
            print("+ ", end="")
        else:
            print("= ", jumlah_3010, end="")
print()
print("jumlah_3010 =", jumlah_3010)
