# Nama: Muhammad Farhan Amri
# NIM: 2611533010
# Bonus: Palindrom Kalimat

kalimat = input("Masukkan kalimat: ")

# Mengubah huruf menjadi kecil dan menghapus spasi
bersih = kalimat.lower().replace(" ", "")

# Memeriksa palindrom
if bersih == bersih[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")