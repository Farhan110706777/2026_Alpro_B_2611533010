# Buat file dengan nama lainnya_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Program operator keanggotaan dan identitas

print("==================================")
print("1. OPERATOR KEANGGOTAAN")
print("==================================")

# Input beberapa data yang dipisahkan dengan koma
input_data_3010 = input("Masukkan beberapa angka, pisahkan dengan koma: ")

# Mengubah input menjadi list integer
data_3010 = [int(angka.strip()) for angka in input_data_3010.split(",")]

nilai_dicari_3010 = int(input("Masukkan angka yang ingin dicari: "))

# Operator in
hasil_3010 = nilai_dicari_3010 in data_3010
print("\nOperator keanggotaan IN")
print(nilai_dicari_3010, "in", data_3010, "=", hasil_3010)

# Operator not in
hasil_3010 = nilai_dicari_3010 not in data_3010
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari_3010, "not in", data_3010, "=", hasil_3010)

print("\n==================================")
print("2. OPERATOR IDENTITAS")
print("==================================")

# objek1 menggunakan list dari input pengguna
objek1_3010 = data_3010

# objek2 merujuk pada objek yang sama dengan objek1
objek2_3010 = objek1_3010

# objek3 memiliki isi sama, tetapi merupakan objek baru
objek3_3010 = data_3010.copy()

print("objek1_3010 =", objek1_3010)
print("objek2_3010 =", objek2_3010)
print("objek3_3010 =", objek3_3010)

# Operator is
hasil_3010 = objek1_3010 is objek2_3010
print("\nOperator identitas IS")
print("objek1_3010 is objek2_3010 =", hasil_3010)

# Operator is not
hasil_3010 = objek1_3010 is not objek3_3010
print("\nOperator identitas IS NOT")
print("objek1_3010 is not objek3_3010 =", hasil_3010)

# Membandingkan identitas dan nilai
print("\nPerbandingan identitas dan nilai")
print("objek1_3010 is objek3_3010 =", objek1_3010 is objek3_3010)
print("objek1_3010 == objek3_3010 =", objek1_3010 == objek3_3010)