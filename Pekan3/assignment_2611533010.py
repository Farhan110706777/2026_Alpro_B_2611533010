# Buat file dengan nama assignment_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator assignment dalam Python

angka1_3010 = int(input("Input angka-1: "))
angka2_3010 = int(input("Input angka-2: "))

print("\nNilai awal angka1_3010 =", angka1_3010)
print("Nilai angka2_3010 =", angka2_3010)

# Assignment biasa
hasil = angka1_3010
print("\nAssignment biasa (=)")
print("Hasil =", hasil)

# Assignment penambahan
hasil = angka1_3010
hasil += angka2_3010
print("\nAssignment penambahan (+=)")
print("Hasil =", hasil)

# Assignment pengurangan
hasil = angka1_3010
hasil -= angka2_3010
print("\nAssignment pengurangan (-=)")
print("Hasil =", hasil)

# Assignment perkalian
hasil = angka1_3010
hasil *= angka2_3010
print("\nAssignment perkalian (*=)")
print("Hasil =", hasil)

# Assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_3010 != 0:
    hasil = angka1_3010
    hasil /= angka2_3010
    print("\nAssignment pembagian (/=)")
    print("Hasil =", hasil)
    # Operator tambahan
    hasil = angka1_3010
    hasil //= angka2_3010
    print("\nAssignment pembagian bulat (//=)")
    print("Hasil =", hasil)
    hasil = angka1_3010
    hasil %= angka2_3010
    print("\nAssignment sisa bagi (%=)")
    print("Hasil =", hasil)
else:
    print("\nPembagian tidak dapat dilakukan.")
    print("Angka kedua tidak boleh bernilai 0.")

# Operator tambahan: assignment perpangkatan
hasil = angka1_3010
hasil **= angka2_3010
print("\nAssignment perpangkatan (**=)")
print("Hasil =", hasil)