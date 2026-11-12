# Nama: Muhammad Farhan Amri
# NIM: 2611533010
# Pertanyaan 5

nama_pengguna = input("Nama pengguna: ")

if len(nama_pengguna) < 5:
    print("Tidak valid: minimal 5 karakter")
elif not nama_pengguna.isalnum():
    print("Tidak valid: hanya huruf dan angka")
elif not nama_pengguna[0].isalpha():
    print("Tidak valid: harus diawali dengan huruf")
else:
    print("Valid")

# Nama: Muhammad Farhan Amri
# NIM: 2611533010
# Bagian B: NIM

nim = input("NIM: ")

if len(nim) == 10 and nim.isdigit():
    tahun = "20" + nim[:2]
    print(f"Valid, intake year {tahun}")
else:
    print("Invalid NIM")