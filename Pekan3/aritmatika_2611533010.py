# Buat file dengan nama aritmatika_NIM.py
# Buat program untuk operator aritmatika dalam python
# Nama variabel ditambah 4 digit NIM terakhir contoh: angka_1234
# Program ini menggunakan fungsi input ()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer

angka1_3010 = int(input("Input angka-1: "))
angka2_3010 = int(input("Input angka-2"))

# Penjumlahan
hasil = angka1_3010 + angka2_3010
print("\nOperator Penjumlahan")
print("Hasil =", hasil)

# Pengurangan
hasil = angka1_3010 - angka2_3010
print("\nOperator Pengurangan")
print("Hasil =", hasil)

# Perkalian
hasil = angka1_3010 * angka2_3010
print("\nOperator Perkalian")
print("Hasil =", hasil)

# Pembagian, Pembagian bulat, dan Sisa bagi
if angka2_3010 != 0 :
   hasil = angka1_3010 / angka2_3010
   print("\nOperator Pembagian")
   print("Hasil =", hasil)

   hasil = angka1_3010 // angka2_3010
   print("\nOperator Pembagian Bulat")
   print("Hasil =", hasil)

   hasil = angka2_3010 % angka2_3010
   print("\nOperator Sisa Bagi")
   print("Hasil =", hasil)
else:
   print(" Angka kedua tidak boleh bernilai 0")

# Pangkat
hasil = angka1_3010 ** angka2_3010
print("\nOperator Pangkat")
print("Hasil =", hasil)

