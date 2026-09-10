# Buat file dengan nama Konstanta_NIM.py
# Program ini menggunakan konstanta untuk menghitung luas lingkaran
# Nama variabel ditambah 4 digit nim terakhir contoh: jari_1234

from typing import Final
PI: Final = 3.14 
print("pi: %f" % (PI))
jari_3010 = float (input("Masukkan nilai jari-jari: '))
luas_3010 = PI * jari_3010 * jari_3010
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_3010, luas_3010))
      