# Buat file dengan nama Logika_NIM.py
# Nama variabel ditambah 4 digit NIM terakhir contoh: a1_1234
# Program ini menggunakan fungsi input ()
# Program operator logika dalam Python

# Memasukkan nilai boolean
# Input tidak peka terhadap huruf besar dan kecil
a1_3010 = input("Input nilai boolean-1 (true/false): ").strip().lower() == "true"
a2_3010 = input("Input nilai boolean-2 (true/false): ").strip().lower() == "true"

print("\nA1 =", a1_3010)
print("A2 =", a2_3010)

# Konjungsi: bernilai True jika keduanya True
hasil = a1_3010 and a2_3010
print("\nKonjungsi (AND)")
print("A1 and A2 =", hasil)

# Disjungsi: bernilai True jika salah satunya True
hasil = a1_3010 or a2_3010
print("\nDisjungsi (OR)")
print("A1 or A2 =", hasil)

# Negasi A1: membalik nilai A1
hasil = not a1_3010
print("\nNegasi A1 (NOT)")
print("not A1 =", hasil)

# Negasi A2: membalik nilai A2
hasil = not a2_3010
print("\nNegasi A2 (NOT)")
print("not A2 =", hasil)

# XOR: bernilai True jika kedua nilai berbeda
hasil = a1_3010 != a2_3010
print("\nDisjungsi Eksklusif (XOR)")
print("A1 XOR A2 =", hasil)