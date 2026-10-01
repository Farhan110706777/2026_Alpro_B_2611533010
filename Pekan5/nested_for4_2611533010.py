# Buat file dengan nama nested_for4_NIM.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh : ulang_3010
# Program ini menggunakan fungsi input ()

tinggi_3010 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_3010 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_3010 = tinggi_3010
    c_3010 = a_3010
    lebar_3010 = (2 * tinggi_3010) - 2

    for i_3010 in range(1, tinggi_3010 + 1):
        b_3010 = c_3010 + 1

        for j_3010 in range(1, lebar_3010 + 1):

            # Baris atas dan bawah
            if i_3010 == 1 or i_3010 == tinggi_3010:
                if j_3010 == 1 or j_3010 == lebar_3010:
                    print("#", end="")
                else:
                    print("=", end="")
                    # Baris isi
            else:
                if j_3010 == 1 or j_3010 == lebar_3010:
                    print("|", end="")
                else:
                    if j_3010 == c_3010:
                        print("<", end="")
                    elif j_3010 == b_3010:
                        print(">", end="")
                    elif j_3010 == (lebar_3010 - c_3010):
                        print("<", end="")
                    elif j_3010 == (lebar_3010 - c_3010 + 1):
                        print(">", end="")
                    elif j_3010 > b_3010 and j_3010 < (lebar_3010 - c_3010):
                        print(".", end="")
                    else:
                        print(" ", end="")

        print()

        # Logika asli Java
        a_3010 -= 2

        if a_3010 <= 0:
            c_3010 = (-a_3010) + 2
        else:
            c_3010 = a_3010