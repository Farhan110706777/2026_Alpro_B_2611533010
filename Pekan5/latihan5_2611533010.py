# Tugas: Program untuk menampilkan pola segitiga sama kaki menggunakan perulangan for
# Nama variabel disesuaikan dengan 4 digit NIM terakhir (3010)

tinggi_3010 = int(input("Masukkan tinggi segitiga: "))

for i_3010 in range(1, tinggi_3010 + 1):
    # Cetak spasi untuk membuat posisi bintang di tengah (terpusat)
    print(" " * (tinggi_3010 - i_3010), end="")
    
    # Cetak bintang diikuti spasi
    print("* " * i_3010)